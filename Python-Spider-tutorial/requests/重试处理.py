# _*_ coding: utf-8 _*_
import requests
from retrying import retry

# 2. 使用装饰器进行重试设置
# stop_max_attempt_number 表示重试次数
@retry(stop_max_attempt_number = 3)
def parse_url(url):
    print("访问的url:", url)
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"
    }
    proxies = {
        'http':'124.235.135.210:80'
    }
    response = requests.get(url, headers=headers, proxies=proxies, timeout=5)
    return response.text

if __name__ == '__main__':
    url = "www.baidu.com"
    try:
        html = parse_url(url)
        print(html)
    except Exception as e:
        print(e)



