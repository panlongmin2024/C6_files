import base64
import binascii
import hashlib
import time
import requests
import uuid
from binascii import a2b_hex
from serial import Serial
from time import sleep
import threading


def main_func(port: str, baud: int, stop_bits: int):
    sleep(2)
    com = Serial(port=port, baudrate=baud, stopbits=stop_bits)
    com.set_buffer_size(2048, 2048)
    print('open port')
    # 'user enter_uart_test'
    com.write(a2b_hex('7573657220656e7465725f756172745f'))
    sleep(0.1)
    com.write(a2b_hex('746573740d'))
    sleep(0.3)
    com.flushInput()
    sleep(0.3)
    # 'WLT_READ_UUID'
    com.write(a2b_hex('574c545f524541445f555549440D'))
    sleep(0.2)
    uuid1 = com.read(45)
    print(uuid1)
    uuid_org = str(uuid1)
    print(uuid_org)
    uuid2 = uuid_org[15:-1]
    print(uuid2)
    print("uuid_string:" + uuid2)
    hash_value = sha256_hash(uuid2)
    signature, msg = send_hash_for_signing('http://192.168.1.100:8001/sign-firmware-development', hash_value)
    com.flushInput()
    random_string = str(uuid.uuid4()).replace('-', '')[:512]
    key_cmd = 'WLT_HASH_UUID=' + signature
    # key_cmd=
    key_hex = key_cmd.encode().hex()
    print('key_cmd: ' + key_cmd)
    print('instruct: ' + key_hex)
    print('write key in')
    com.write(a2b_hex(key_hex))
    print(com.read(10))
    t1 = threading.Thread(target=keep_read, args=(com,))
    t2 = threading.Thread(target=turn_off, args=(com,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    return uuid2, hash_value, key_cmd


# def create_uuid_file(file_path):
#     # 读uuid32位值
#     random_string = str(uuid.uuid4()).replace('-', '')[:32]
#     with open(file_path, 'w') as file:
#         file.write(random_string)
#     return random_string
#
#
# def create_uuid_file2(uuid: str, file_path: str):
#     with open(file_path, 'w') as file:
#         file.write(uuid)
#     return uuid


# def get_file_size(file_path):
#     # 获取文件大小
#     return os.path.getsize(file_path)


# def get_sha256_hash(file_path):
#     result = subprocess.run(['certutil', '-hashfile', file_path, 'sha256'], capture_output=True, text=True)
#     stdout = result.stdout
#     print(stdout)
#     pattern = r'(\n.*?\n)'
#     matches = re.findall(pattern, stdout)
#     hash_value = matches[0].replace("\n", "")
#     return hash_value


def send_hash_for_signing(server_url, hash_value, ):
    print('hash_value:' + hash_value)
    data = {
        "hashOfFirmwareImage": hash_value,
        "productModelName": "JBL Test Speaker"
    }
    print("向树莓派发送请求,url: " + server_url)
    response = requests.post(url=server_url, json=data)

    print("response:" + response.text)
    if response.status_code == 200:
        response_data = response.json()
        if 'signature' in response_data:
            signature = response_data['signature']
            return change_to_hex(signature), ''
        else:
            return None, "error: no signature uuid_cert word in response"
    else:
        print("5")
        return None, response.text


def change_to_hex(base64_str):
    # 解码base64字符串
    decoded_data = base64.b64decode(base64_str)

    # 将解码后的数据转换为16进制字符串
    hex_str = binascii.hexlify(decoded_data).decode('utf-8')

    print('hex_key: ' + hex_str)
    print('hex_key len: ' + str(len(hex_str)))
    return hex_str


def sha256_hash(s):
    return hashlib.sha256(s.encode('utf-8')).hexdigest()


# def sign_file(signature, output_path):
#     with open(output_path, 'wb') as signature_file:
#         signature_file.write(signature)


def keep_read(com):
    try:
        result: str = '未读到验签log'
        result_data: str = ''
        # 开始时间
        start_time = time.time()
        while True:
            if com.in_waiting > 0:
                msg: bytes = com.readline()
                if b'uuid verify ok' in msg:
                    print(msg)
                    result_data = str(msg)[2:-7]
                    result = '验签成功'
                    break
                elif b'uuid verify fail' in msg:
                    result = '验签失败'
                    break
                # 检查是否已经过去了5秒
                if time.time() - start_time >= 5:
                    break
        print(result_data)
        print(result)
    except Exception as e:
        print(e)


def turn_off(com):
    try:
        com.flushInput()
        print('restart')
        com.write(data=a2b_hex('TL_DUT_REBOOT'.encode().hex()))
    except Exception as e:
        print(e)


# # main_func('COM5', baud=3000000,stop_bits=1)
if __name__ == '__main__':
    main_func('COM5', baud=3000000, stop_bits=1)
