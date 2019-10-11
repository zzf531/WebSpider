import requests

# 定义请求地址
url = 'http://www.baidu.com'

# 发送get请求获取响应
response = requests.get(url)

# 获取响应的html内容
html = response.text

print(html)

