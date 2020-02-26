import requests
import urllib3
import logging

urllib3.disable_warnings()  # 它建议我们给它指定证书
response = requests.get('https://www.12306.cn', verify=False)
print(response.status_code)


logging.captureWarnings(True)  # 或者通过捕获警告到日志的方式忽略警告：
response2 = requests.get('http://www.12306.cn', verify=False)
print(response2.status_code)
