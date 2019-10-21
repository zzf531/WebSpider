# 导入re模块
import re

print("正则表达式\d操作")
# 数字[0-9]
ret = re.match("嫦娥\d号", "嫦娥3号发射失败")
print(ret.group())

print("正则表达式\D操作")
# 匹配非数字[^0-9]
match_obj = re.match("\D", "。")
if match_obj:
    print(match_obj.group())
else:
    print("匹配失败")

# \s 空白字符:[<空格>\t\r\n\f\v]
match_obj = re.match("hello\sworl")

