#!/usr/bin/python
# -*- coding:utf-8 -*-
# -------------------------------------------------------------------------------
# Name:        efuse.py
# Purpose:
#
# Author:      wuyufan
#
# Created:     04-05-2015
# Copyright:   2014-2015 Actions (Zhuhai) Technology Co., Limited,
# Licence:     <your licence>
# -------------------------------------------------------------------------------
import json
import subprocess
import os
import sys
import requests
import base64

# server_url = 'http://192.168.4.208:8001/sign-firmware-development'  # server url
server_url = 'http://192.168.40.101:8001/sign-firmware-development'


def get_sha256_hash(file_path):
    # cmd = ['openssl', 'dgst', '-sha256', file_path]
    cmd = ['certutil', '-hashfile', '../uuid.txt']
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True, universal_newlines=True)
    print(result)
    hash_str = result.stdout.strip().split('\n')[0]

    print(hash_str)
    hash_value = hash_str.split('=')[1].strip()
    print(hash_value)
    return hash_value


def send_file_for_signing(server_url, file_path):
    try:
        hash_string = get_sha256_hash(file_path)
        print(hash_string)
        data = {
            "hashOfFirmwareImage": hash_string,
            "productModelName": "JBL Test Speaker"
        }
        # print(data)
        response = requests.post(server_url, json=data)
        if response.status_code == 200:
            print("request ok\n")
            try:
                response_data = response.json()
                if 'signature' in response_data:
                    # print("sign data: ", response_data['signature'])
                    signature = response_data['signature']
                    binary_data = base64.b64decode(signature)
                    return binary_data
                else:
                    print("error: no signature uuid_cert word in response")
            except json.JSONDecodeError:
                print("error: not jason data")
        else:
            print("request failed, status code: ", response.status_code)

        return None
    except requests.RequestException as e:
        print(f"An error occurred while sending data for signing: {e}")
        return None


def sign_file(file_path, output_path):
    # if os.path.exists(output_path):
    #    print(f"sign file %s existed" %(output_path))
    #    return

    signature = send_file_for_signing(server_url, file_path)

    with open(output_path, 'wb') as signature_file:
        signature_file.write(signature)


def verify_signature(public_key_path, file_path, signature_path):
    try:
        if not os.path.exists(public_key_path):
            print(f"uuid_cert file %s not existed" % (public_key_path))
            return

        with open(file_path, 'rb') as file_to_verify, open(signature_path, 'rb') as signature_file:
            cmd = ['openssl', 'dgst', '-sha256', '-verify', public_key_path, '-signature', signature_path]
            subprocess.run(cmd, stdin=file_to_verify, check=True)

        print(f"Signature of {file_path} is valid.")
    except subprocess.CalledProcessError:
        print(f"Signature of {file_path} is invalid.")
    except Exception as e:
        raise Exception(f"An error occurred while verifying the signature: {e}")


def merge_app_file(original_file, cert_file, file_to_sign):
    with open(original_file, 'rb') as file1:
        data1 = file1.read()

    with open(cert_file, 'rb') as file2:
        data2 = file2.read()

    with open(file_to_sign, 'wb') as merged_file:
        merged_file.write(data1)
        merged_file.write(data2)


def rsa_sign_app_file(original_file, cert_file, file_to_sign, key_path):
    sign_file(original_file, cert_file)

    verify_signature(key_path, original_file, cert_file)

    merge_app_file(original_file, cert_file, file_to_sign)


def main(argv):
    rsa_sign_app_file(argv[1], argv[2], argv[3], argv[4])


if __name__ == "__main__":
    # main(sys.argv)
    get_sha256_hash('11')