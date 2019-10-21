# -*- coding: utf-8 -*-
import json

json_string =[
    {
        "monther": "妈妈",
        "father": "爸爸",
    },
    {
        "monther": "妈妈",
        "father": "爸爸",
    }
]

print(type(json_string))
json_string2 = json.dumps(json_string)
print("json_strong数据类型:", type(json_string2))
