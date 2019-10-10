import requests

keyword = "刘德华"
url = "http://www.baidu.com/s?ie=UTF-8"

try:
    kv = {"wd":keyword}
    r = requests.get(url, params=kv)
    print(r.request.url)
    r.raise_for_status()
    print(len(r.text))
    print(r.text[1000:2000])

except:
    print('爬去失败')

