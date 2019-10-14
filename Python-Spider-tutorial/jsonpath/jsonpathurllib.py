from urllib import request
# json解析库，对应xml
import json
# json的解析语法，对应xpath
import jsonpath

url = "http://www.lagou.com/lbs/getAllCitySearchLabels.json"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:67.0) Gecko/20100101 Firefox/67.0"}
my_request = request.Request(url, headers=headers)
response = request.urlopen(my_request)
# 取出json文件里的内容，返回的格式是字符串
html = response.read()

