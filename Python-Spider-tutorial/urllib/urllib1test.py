# _*_ coding: utf-8 _*_

import urllib.request

# 发起网络请求， 定义请求链接
url = "https://www.githup.com"

# 定义请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36",
    "Referer": "https://githup.com/",
    "Host": "githup.com"
}

# 定义请求对象
req = urllib.request.Request(
    url = url,
    headers = headers
)

# 发送请求
resp = urllib.request.urlopen(req)

# 处理请求
with open('githup.txt', 'wb') as f:
    f.write(resp.read())





