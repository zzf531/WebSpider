import json

str = '''
[{
    "name": "Bob",
    "gender": "male",
    "birthday": "1992-10-18"
}, {
    "name": "Selina",
    "gender": "female",
    "birthday": "1995-10-18"
}]
'''
print(type(str))
data = json.loads(str)
print(data)
print(type(data))

print(data[0]['name'])  # data[0].get('name') 一种是中括号加键名，
# 另一种是通过 get 方法传入键名,推荐使用 get 方法，这样如果键名不存在，则不会报错，
# 会返回 None。另外，get 方法还可以传入第二个参数（即默认值），示例如下：
print('--------------------')
data[0].get('age')
data[0].get('age', 25)


with open('data.json', 'r') as f:
    str = f.read()
    print(type(str))
    data = json.loads(str)
    print(data)



