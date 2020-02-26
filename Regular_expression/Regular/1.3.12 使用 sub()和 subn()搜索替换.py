import re
m = re.sub('X', '小飞机', 'attn: X  Dear X')
print(m)

m2 = re.subn('X', '小玲玲', 'attn: XDear X,')
print(m2)

m3 = re.sub('[ac]', '一', 'abcde'); print(m3)
m4 = re.subn('[ac]', '一', 'abcde'); print(m4)

m5 = re.sub(r'(\d{1,2})/(\d{1,2})/(\d{2}|\d{4})',r'\2/\1/\3', '2/20/1991')
print(m5)

m6 = re.sub(r'(\d{1,2})/(\d{1,2})/(\d{2}|\d{4})',r'\2/\1/\3', '2/20/1991')
print(m6)