import requests

url = 'http://www.baidu.com'

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
}

# 定义cookie的值
cookies = {
    "xx": "yy"
}

# 使用 POST请求参数
response = requests.get(url, headers=headers, cookies=cookies)
print(len(response.text))

