from turtle import pos
from typing import Dict, TypedDict
import requests
import traceback

s = requests.session()
s.keep_alive = False  # 关闭多余连接


class PostCurrentData(object):
    @staticmethod
    def post_permit(post_message):
        return requests.post(
            url="http://192.168.0.6:8000/api/blade-auth/oauth/token?tenantId=800300&username=admin&password"
                "=87ca5a51821455a602b9a522c1188722&grant_type=password&scope=all&type=account",
            headers={
                "Authorization": post_message["Authorization"],  # 授权码
                "Tenant-id": post_message["tenant_id"]
            }
            # 租户id
            # params={
            #     "tenantId": post_message["tenant_id"],
            #     "username": post_message["username"],
            #     "password": post_message["password"],
            #     "grant_type": post_message["grant_type"],
            #     "scope": post_message["scope"],
            #     "type": post_message["type"]
            # },

        )

    # post过站
    @staticmethod
    def pass_station(request_pass_message, token_message):
        return requests.post(
            url="http://192.168.0.6:8000/api/mes-product/public/station/center/test",
            headers={
                "Authorization": "bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9",  # 授权码
                "Blade-Auth": "bearer " + token_message,  # token
                "Content-Type": "application/json;charset=UTF-8"
            },
            data=request_pass_message
        )

    # 上传结果
    @staticmethod
    def upload_test_result(post_set_value, post_message, token_message):
        p_result = requests.post(
            url="http://" + post_set_value['web_url'] + "/api/mes-product/public/station/center/test",
            headers={"Authorization": post_set_value['Authorization'],  # 授权码
                     "Blade-Auth": "bearer " + token_message['access_token'],  # token
                     "Content-Type": "application/json;charset=UTF-8"},
            json=post_message
        )
        post_result = p_result.json()
        return post_result


class PostData(TypedDict):
    Authorization: str
    workOrderNo: str
    routeCode: str
    machineCode: str
    tenant_id: str
    username: str
    password: str
    grant_type: str
    scope: str
    typing: str
    web_url: str


class PostTestData(object):

    def post_permit(self, post_data: dict):
        return requests.post(
            timeout=3,
            url="http://{}/api/blade-auth/oauth/token".format(post_data['web_url']),
            headers={
                "Authorization": post_data["Authorization"],  # 授权码
                "Tenant-id": post_data["tenant_id"]
            },  # 租户id
            params={
                "tenantId": post_data["tenant_id"],
                "username": post_data["username"],
                "password": post_data["password"],
                "grant_type": post_data["grant_type"],
                "scope": post_data["scope"],
                "type": post_data["typing"]
            }

        )

    def pass_station(self, url: str, config_data: dict, token: str, sn) -> requests.Response:
        s = requests.session()
        s.keep_alive = False  # 关闭多余连接
        data: dict = {}
        for i in ["workOrderNo", "stationCode", "routeCode"]:
            data[i] = config_data[i]
        data["sequenceNumber"] = sn
        return s.post(
            url=url,
            headers={
                "Authorization": config_data['Authorization'],  # 授权码
                "Blade-Auth": "bearer " + token,  # token
                "Content-Type": "application/json;charset=UTF-8"
            },
            json=data
        )

    def upload_data(self, result: dict[str], post_data: dict, sequenceNumber: str, token: str) -> requests.Response:
        s = requests.session()
        s.keep_alive = False  # 关闭多余连接
        return s.post(
            url="http://{}/api/mes-product/public/station/center/test".format(post_data['web_url']),
            headers={
                "Authorization": post_data['Authorization'],  # 授权码
                "Blade-Auth": "bearer " + token,  # token
                "Content-Type": "application/json;charset=UTF-8"
            },
            json={
                "workOrderNo": post_data['workOrderNo'],
                "stationCode": post_data['stationCode'],
                "routeCode": post_data['routeCode'],
                "sequenceNumber": sequenceNumber,
                "eventResult": "PASS",
                "failureCode": "CZ001",
                "extendSequenceNumber": "",
                "machineTestData": {
                    "machineCode": post_data["machineCode"],
                    "titles": {"电脑IP": "100",
                               "测试产品": "200",
                               "彩盒SN": "300",
                               "地区SN": "400",
                               "重量g": "500",
                               "重量g范围": "600"},
                    "results": [result]
                }
            }
        )

    @staticmethod
    def post(url, **kwargs):
        """封装post方法"""
        # 获取请求参数
        params = kwargs.get("params")
        json = kwargs.get("json")
        headers = kwargs.get("headers")
        try:
            s = requests.session()
            s.keep_alive = False  # 关闭多余连接
            result = s.post(url, params=params, headers=headers, json=json)
            return result
        except Exception as e:
            return traceback.format_exc()

    def get(self, url, **kwargs):
        """封装get方法"""
        # 获取请求参数
        headers = kwargs.get("headers")
        try:
            s = requests.session()
            s.keep_alive = False  # 关闭多余连接
            result = s.get(url, headers=headers)
            return result
        except Exception as e:
            return traceback.format_exc()
