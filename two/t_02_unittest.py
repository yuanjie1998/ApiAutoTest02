import requests
import unittest


class loginCase(unittest.TestCase):
    def setUp(self):
        self.session = requests.Session()
        self.login_url = "http://191.0.0.200:5807/sso/aaa.action?sUrl=/lgywsoft/emergencyDuty/index.action"

    def tearDown(self):
        self.session.close()

    def test01_success(self):
        login_data = {
            "loginName": "值班员新",
            "loginPass": "12345678",
            "ajax": "true",
            "rememberPassword": ""
        }
        response = self.session.post(url=self.login_url, data=login_data)
        print(response.json())
        self.assertEqual(1000, response.json().get("errorCode"))
        self.assertIn("access_token", response.json().get("errorMsg"))

    def test02_Username_error(self):
        login_data = {
            "loginName": "值班员新0",
            "loginPass": "12345678",
            "ajax": "true",
            "rememberPassword": ""
        }
        response = self.session.post(url=self.login_url, data=login_data)
        print(response.json())
        self.assertEqual(1003, response.json().get("errorCode"))
        self.assertIn("用户名或密码不正确", response.json().get("errorMsg"))

    def test03_password_error(self):
        login_data = {
            "loginName": "值班员新",
            "loginPass": "123456789",
            "ajax": "true",
            "rememberPassword": ""
        }
        response = self.session.post(url=self.login_url, data=login_data)
        print(response.json())
        self.assertEqual(1003, response.json().get("errorCode"))
        self.assertIn("用户名或密码不正确", response.json().get("errorMsg"))

    def test04_usepwd_none(self):
        login_data = {
            "loginName": "",
            "loginPass": "",
            "ajax": "true",
            "rememberPassword": ""
        }
        response = self.session.post(url=self.login_url, data=login_data)
        print(response.json())
        self.assertEqual(1003, response.json().get("errorCode"))
        self.assertIn("用户名或密码不正确", response.json().get("errorMsg"))

    # 定义方法
    def siyou(self, name, age):
        print("%s已进入....今年%d岁" % (name, age))
        print("%s已进入..." % name)
