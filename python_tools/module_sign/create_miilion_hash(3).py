import base64
import binascii
import hashlib
import os
import re
import subprocess
import requests
import uuid
from binascii import a2b_hex
from serial import Serial
from time import sleep


def get_uuid(port: str, baud: int) -> None:
    sleep(2)
    com = Serial(port=port, baudrate=baud)
    print('open')
    instruct = 'user enter_uart_test'
    com.write(a2b_hex('7573657220656e7465725f756172745f'))
    sleep(0.1)
    com.write(a2b_hex('746573740d'))
    sleep(1)
    com.flushInput()
    instruct2 = 'WLT_READ_UUID'
    com.write(a2b_hex('574c545f524541445f555549440D'))

    uuid1 = com.read(45).decode()
    print(uuid1)
    uuid2 = uuid1[13:-1] + uuid1[-1]
    print(uuid2)
    uuid_string = create_uuid_file2(uuid2, out_put_path)
    print("uuid_string:" + uuid_string)
    # if get_file_size(uuid_file_path) == 32:
    # hash_value = get_sha256_hash(uuid_file_path)
    hash_value = sha256_hash(uuid_string)
    with open('hash_file.txt', 'a') as file:
        file.write(hash_value + '\n')
    # send_file_for_signing('http://192.168.1.101:8001/sign-firmware-development', hash_value)
    signature, msg = send_file_for_signing('http://192.168.1.100:8001/sign-firmware-development', hash_value, )
    # if signature is not None:
    #     sign_file(signature, out_put_path)
    com.flushInput()
    key_cmd = 'WLT_HASH_UUID=' + signature
    key_hex = key_cmd.encode().hex()
    print('key_cmd: ' + key_cmd)
    print('key_hex: ' + key_hex)
    print('write key in ')
    com.write(a2b_hex(key_hex))
    print(com.read(10))
    # else:
    #     print('uuid.txt大小不为32')


def create_uuid_file(file_path):
    # 读uuid32位值
    random_string = str(uuid.uuid4()).replace('-', '')[:32]
    with open(file_path, 'w') as file:
        file.write(random_string)
    return random_string


def create_uuid_file2(uuid: str, file_path: str):
    with open(file_path, 'w') as file:
        file.write(uuid)
    return uuid


def get_file_size(file_path):
    # 获取文件大小
    return os.path.getsize(file_path)


def get_sha256_hash(file_path):
    result = subprocess.run(['certutil', '-hashfile', file_path, 'sha256'], capture_output=True, text=True)
    stdout = result.stdout
    print(stdout)
    pattern = r'(\n.*?\n)'
    matches = re.findall(pattern, stdout)
    hash_value = matches[0].replace("\n", "")
    return hash_value


def send_file_for_signing(server_url, hash_value, ):
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
            # change_to_hex(signature)
            # binary_data = base64.b64decode(signature)

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


def sign_file(signature, output_path):
    with open(output_path, 'wb') as signature_file:
        signature_file.write(signature)


out_put_path = './key/key.bin'
uuid_file_path = './uuid/uuid.txt'
# for i in range(20000):
# uuid_string = create_uuid_file(uuid_file_path)
get_uuid('COM5', baud=3000000)

# break

# 45 42 f9 0c 75 00 c3 76 a9 39 f4 4f 1a 6b f8 5e
# b1 46 dd 83 02 d2 90 86 53 cc d4 95 7b d0 9d 0e

'5668ebe606d72322f601a3049347d0e980b13ee1a8bece8b9890139034f9e7b0'
# 5668ebe606d72322f61 a3049347 d0 e9
# 80b3eela8be ce8h989139034 f9e7 b0
