import re
print(re.findall('car', 'car'))
print(re.findall('car', 'scary'))
print(re.findall('car', 'carry the barcardi to the car'))

'''
findall()查询字符串中某个正则表达式模式全部的非重复出现情况

'''

s = 'This and that'
m = re.findall(r'(th\w+) and (th\w+)', s, re.I)  # re.I不区分大小写
# print(m)

m1 = re.finditer(r'(th\w+) and (th\w+)', s, re.I)
# print(next(m1).groups())
# print(next(m1).group(1))
g = next(m1)
print(g.groups())

