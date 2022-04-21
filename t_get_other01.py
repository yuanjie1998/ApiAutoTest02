import requests


class yingJi():

    def dengLu(name, age):
        print("%s 已进入，%d 岁...." % (name, age))
        print("--" * 200)
        response = requests.get("http://191.0.0.65:5807/")

        headers = response.headers
        print("请求头信息为：", headers)
        print("Content-Type：", headers.get("Content-Type"))

        print(response.cookies)
        print("JSESSIONID为：", response.cookies.get("JSESSIONID"))

        print(response.encoding)
        print(response.status_code)
        print(response.url)

        print("--" * 200)
        print(response.text)


if __name__ == "__main__":
    print(yingJi.dengLu("老王", 50))