from lxml import etree

html = etree.parse('./test.html', etree.HTMLParser())
result = html.xpath('//*')
print(result)


result = html.xpath('//li')
print(result)
print(result[0])


result = html.xpath('//li/a')
print(result)