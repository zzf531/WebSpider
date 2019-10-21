# -*- coding: utf-8 -*-
# 网络获取数据
import requests
import json
import jsonpath

url = "http://122.51.48.30:3000/artist/list?cat=1001"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
}

response = requests.get(url,headers=headers)
html = response.text
print(html)
# 把响应数据转换成python数据类型
data = json.loads(html)

# 使用 jsonpath 提取数据
cities = jsonpath.jsonpath(data, '$..name')
ids = jsonpath.jsonpath(data, '$..id')
dictionary = dict(zip(cities, ids))
with open('data_out1.json','w',encoding='utf-8') as f:
    json.dump(dictionary, f, ensure_ascii=False, indent=2)
print(dictionary)



