# coding=utf-8

import re
ret = re.match(".", "M")
print(ret.group())

ret = re.match("t.o", "too")
print(ret.group())

ret = re.match("h", "hello Python")
print(ret.group())

# 大小写都可以匹配
ret = re.match("[hH]", "hello Python")
print(ret.group())
ret = re.match("[hH]ello Python", "hello Python")
print(ret.group())
print("*" * 100)

# 匹配0到9的两种写法
ret = re.match("[0-9]", "7")
print(ret.group())

ret = re.match('[0123456789]', '7')
print(ret.group())

# match区间[0,3] [8,9]
ret = re.match("[0-38-9]Hello Python","3Hello Python")
print(ret.group())

# 下面这个正则不能够匹配到数字4，因此ret为None
ret = re.match("[0-35-9]Hello Python","4Hello Python")
# print(ret.group())
print('*' * 100)



