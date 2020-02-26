import re
a = 'zzf531   tty7         2020-01-09 16:17 (:0)'
print(re.split(r'\s\s+', a))  # \s 匹配空格字符

data = 'Thu Feb 15 17:46:04 2007::uzifzf@dpyivihw.gov::1171590364-6-8'
patt = '^(Mon|Tue|Wed|Thu|Fri|Sat|Sun)'
m = re.match(patt, data)
print(m.group(1))
# print(m.group())
# print(m.groups())

patt2 = '^(\w{3})'
m2 = re.match(patt2, data)
print(m2.group())

