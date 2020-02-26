"""
group()要么返回整个匹配对象,要么根据要求返回特定子组。
groups()返回一个包含唯一或者全部子组的元祖
match() 函数试图从字符串的起始部分对模式进行匹配
匹配成功,就返回一个匹配对象,匹配失败,就返回 None,
匹配对象的 group()方法能够用于显示那个成功的匹配
"""
import re

m = re.match('foo', 'foo')
if m:
    print('m的值', m.group())

print(re.match('foo', 'foo on the table').group())

s = re.search('sea', 'seafood')
if m:
    print(s.group())


# \b 匹配任何边界字符
m1 = re.match('\\bblow', 'blow')  # \b为ASCII字符,加上反斜线转义,就是\b,为正则表达式的特殊字符
if m1: print('m1的值', m1.group())

m1 = re.match(r'\bblow', 'blow')  # r'' 原始输出转义字符, 所以\b变成Python正则特殊符号
if m1: print('m1的值', m1.group())


