import requests
url = "http://m.ip138.com/ip.asp?"
ip = "125.220.159.160"
kv = {"ip":ip}

try:
    r = requests.get(url, params = kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text)
except:
    print("爬取失败")
