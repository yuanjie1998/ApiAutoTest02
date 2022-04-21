import requests
import unittest
"""
集成unittest,登录接口断言
"""
session = requests.Session()
login_url = "http://191.0.0.200:5807/sso/aaa.action?sUrl=/lgywsoft/emergencyDuty/index.action "
login_data = {
    "loginName": "值班员新",
    "loginPass": "12345678",
    "ajax": "true",
    "rememberPassword": ""
}
response = session.post(login_url, data=login_data)
print(response.headers.get("Set-Cookie"))
print(response.status_code)
print(response.json())


