import re

content = 'http://weibo.com/comment/kEraCN'
result1 = re.match('http.*?comment/(.*?)', content)
result2 = re.match('http.*?comment/(.*)', content)
a =result1.group(1)
print('result1',a)
print('result2', result2.group(1))