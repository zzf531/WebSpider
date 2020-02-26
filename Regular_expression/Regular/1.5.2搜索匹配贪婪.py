import re
data = 'Thu Feb 15 17:46:04 2007::uzifzf@dpyivihw.gov::1171590364-6-8'
patt = '.+?(\d+-\d+-\d+)'
patt1 = '\d+-\d+-\d+'
m = re.search(patt1, data)
print(m.group())

m1 = re.match(patt, data)
print(m1.group(1))

print(re.split('::', data)[2])

print('取出三个整数字段中间的那个整数')
patt = '-(\d+)-'
print(re.search(patt, data).group(1))