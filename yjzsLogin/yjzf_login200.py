import requests

session = requests.Session()
login_url = "http://191.0.0.200:5807/sso/aaa.action?sUrl=/lgywsoft/emergencyDuty/index.action "
login_data = {
    "loginName": "值班员新",
    "loginPass": "12345678",
    "ajax": "true",
    "rememberPassword": ""
}
# 1.登录接口
response = session.post(url=login_url, data=login_data)
data = response.json()
print("响应数据为：%s" % data)
# /lgywsoft/emergencyDuty/index.action ?lang=zh&access_token=000001803FB99EF7-BF0000C8-BF000558-313630-B6D2B819-5F21-4DD3-BD79-B3579184CBD4
errorMsg = data.get("errorMsg")
print("errorMsg为：", errorMsg)
# 字符串分割获取access_token
msg_split = errorMsg.split("=")
print("分割后：", msg_split)
print(type(msg_split))
print("*" * 50)
access_token = msg_split[2]
print("分割出的access_token：", access_token)

# 2.领导驾驶舱页面接口拼接,从登录响应数据中获得access_token
login_url02 = "http://191.0.0.200:5807/lgywsoft/emergencyDuty/index.action?lang=zh&access_token=" + access_token
print(login_url02)
# 领导驾驶舱页面请求
response02 = session.get(url=login_url02)
print(response02.text)

print("*" * 50)
# 3.应急值班页面接口(值班首页)
response03 = session.get("http://191.0.0.200:5807/lgywsoft/emergencyDuty/index.action")
# print(response03.text)

# 4.工作办理页面
response04 = session.get("http://191.0.0.200:5807/lgywsoft/toIndex.action")
# print(response04.text)

# 关闭session对象
session.close()
