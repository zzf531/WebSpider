import re
from Regular_expression.Dome.test_serarch import html

result = re.search('<li.*?active.*?singer="(.*?)">(.*?)</a>', html, re.S)
if result:
    print(result.group(1), result.group(2))


result = re.search('<li.*?singers="(.*?)">(.*?)</a>', html, re.S)
if result:
    print(result.group(1), result.group(2))


result = re.search('<li.*?singer="(.*?)">(.*?)</a>', html)
if result:
    print(result.group(1), result.group(2))



result = re.search('<a.*6.*er="(.*)">(.*)</a>', html)
if result:
    print(result.groups())
