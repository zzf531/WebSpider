import requests

url = "http://www.baidu.com/s?"
kw = {
    'wd': '熊猫'
}
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}
rep = requests.get(url, headers=headers)

print(rep.text)
