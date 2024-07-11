import hashlib
import json
import re
import subprocess
import os
import sys
import requests
import base64


def get_sha256_hash(file_path):
    # message = '40da9cf28aaf4b7ebaa8359c75946c3f'
    #
    # # 使用sha256计算消息的哈希值
    # h = hashlib.sha256(message.encode('utf-8'))
    # hex_digest = h.hexdigest()
    # # 如果哈希值的长度已经是偶数，直接返回
    # if len(hex_digest) % 2 == 0:
    #     return hex_digest
    # # 如果长度是奇数，取中间字符
    # elif len(hex_digest) % 2 != 0:
    #     middle = len(hex_digest) // 2
    #     return hex_digest[middle - 1 // 2: middle + 1 // 2]

    result = subprocess.run(['certutil', '-hashfile', file_path, 'sha256'], capture_output=True, text=True)
    stdout = result.stdout
    print(stdout)
    pattern = r'(\n.*?\n)'
    matches = re.findall(pattern, stdout)
    hash_value = matches[0].replace("\n", "")
    return hash_value


def send_file_for_signing(server_url, hash_value, signal):
    signal.emit('hash_value:' + hash_value)
    data = {
        "hashOfFirmwareImage": hash_value,
        "productModelName": "JBL Test Speaker"
    }
    signal.emit("向树莓派发送请求,url: "+server_url)
    response = requests.post(url=server_url, json=data,timeout=3)
    signal.emit("response:"+response.text)
    if response.status_code == 200:
        response_data = response.json()
        if 'signature' in response_data:
            signature = response_data['signature']
            binary_data = base64.b64decode(signature)
            return binary_data, ''
        else:
            return None, "error: no signature uuid_cert word in response"
    else:
        return None, response.text


def sign_file(signature, output_path):
    with open(output_path, 'wb') as signature_file:
        signature_file.write(signature)


if __name__ == '__main__':
    print(get_sha256_hash('../uuid.txt'))
# A4B65D020009
