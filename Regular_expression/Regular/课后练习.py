import re

# 1.匹配字符串bat、hat、bit 等
m = re.match('[bh][aiu]t', 'bat')
print(m.group())

# 2 姓+名
m = re.match('[A-Za-z]+ [A-Za-z]+', 'Zzf cll')
print(m.group())
