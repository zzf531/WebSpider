# -*- coding: utf-8 -*-
import requests
import json
import jsonpath

url = "http://122.51.48.30:3000/artists?id=2116"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
}

response = requests.get(url, headers=headers)
html = response.text
# print(html)
data = json.loads(html)  # python 数据格式
# print(type(data))
a = data['hotSongs']
print(a[0])
print(type(a[0]))
b = a[0]
print(a[1]['name'])
details = []
details.append({
    'name': a[0]['name'],
    'id': a[0]['id']
})
print(details)
ii = 0
while ii <= 20:
    details.append({
        'name': a[ii]['name'],
        'id': a[ii]['id']
    })
    ii += 1
print(details)
with open('single.json', 'w', encoding='utf-8') as f:
    json.dump(details, f, ensure_ascii=False, indent=2)



