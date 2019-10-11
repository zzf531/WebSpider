# 导入模块
import requests
# 定义请求地址
url = 'http://www.baidu.com'
# 定义自定义请求头
headers = {
  "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
}
# 定义 代理服务器
proxies = {
    'http': '140.143.156.166:1080'

}
# 使用 POST 请求参数发送请求
response = requests.get(url,headers=headers,proxies=proxies)
# 获取响应的 html 内容
html = response.text
print(len(html))
print(response.request.headers)
