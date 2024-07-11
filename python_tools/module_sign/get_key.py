import base64

import requests


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
            binary_data = base64.b64decode(signature)

            return binary_data, ''
        else:
            return None, "error: no signature uuid_cert word in response"
    else:
        print("5")
        return None, response.text


out_put_path = './key/key.bin'
send_file_for_signing('http://192.168.1.101:8001/sign-firmware-development',
                      '5668ebe606d72322f601a3049347d0e980b13ee1a8bece8b9890139034f9e7b0')
