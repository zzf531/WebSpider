import requests
from pyquery import PyQuery as pq

url = 'https://www.zhihu.com/explore'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}
html = requests.get(url, headers=headers).text
doc = pq(html)
items = doc('.ExploreSpecialCard-title').items()
print(items)
for item in items:
    question = item.text()
    file = open('explore.txt', 'a', encoding='utf-8')
    file.write(question)
    # file = open('explore.txt', 'a', encoding='utf-8')
    # file.write('\n'.join([question, author, answer]))
    file.write('\n' + '=' * 50 + '\n')
    file.close()