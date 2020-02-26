import re


bt = 'bat|bet|bit'
m = re.match(bt, 'bat')
if m is not None:
    print(m.group())

m1 = re.search(bt, 'He bit me!')
print(m1.group())

# 点号(.) 匹配任何字符,不能匹配一个换行符\n 或者非字符,也就是说,一个空字符串。
anyend = '.end'
m = re.match(anyend, 'bend')
if m is not None: print(m.group())  # bend

m1 = re.match(anyend, 'end')
if m1 is not None: print(m1.group())  # 不匹配任何字符

m2 = re.match(anyend, '\nend')
if m2 is not None: print(m2.group())  # 除了\n之外的任何字符串

patt314 = '3.14'
pi_patt = '3\.14'
m = re.match(patt314, '3.14')
if m is not None: print(m.group())
m1 = re.match(patt314, '3014')
if m1 is not None: print(m1.group())
m2 = re.match(pi_patt, '3.14')
if m2 is not None: print(m2.group())







