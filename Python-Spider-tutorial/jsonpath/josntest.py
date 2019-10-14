# -*- coding: utf-8 -*-
# 导入模块
import json

# json.loads json字符串 转 Python数据类型
json_string = '''
{
    "name": "crise",
    "age": 18,
    "parents": {
        "monther": "妈妈",
        "father": "爸爸"
    }
}
'''
print("json_string数据类型：",type(json_string))
data = json.loads(json_string)
print("data数据类型：",type(data))
print(data)
print('*'*100)

# json.dumps Python 类型数据 转json字符串
data = {
    "name": "crise",
    "age": 18,
    "parents" :{
        "monther": "爸爸",
        "father": "妈妈"
    }
}
print("data数据类型", type(data))
json_string2 = json.dumps(data)
print("json_strong数据类型:", type(json_string2))
print(json_string)
print('#' * 100)

# json.load json文件 转 Python数据类型
with open('data.json','r',encoding='utf-8') as f:
    data = json.load(f)
    print('data数据类型:', type(data))
    print(data)
print('*' * 100)

#json.dump Python数据类型转 json文件
data = {
    "name": "crise",
    "age": 18,
    "parents": {
        "monther": "妈妈",
        "father": "爸爸"
    }
}
with open('data_out.json','w',encoding='utf-8') as f:
    json.dump(data,f,ensure_ascii=False,indent=2)


