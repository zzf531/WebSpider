import requests

r = requests.get('https://www.taobao.com', timeout=1)  # 如果 1 秒内没有响应，那就抛出异常。
print(r.status_code)