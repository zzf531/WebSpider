# 导入re模块
import re

# 使用match方法进行匹配操作
result = re.match(正则表达式, 要匹配的字符串)

# 如果上一步匹配到数据的话，可以使用group方法来提取数据
result.group()
