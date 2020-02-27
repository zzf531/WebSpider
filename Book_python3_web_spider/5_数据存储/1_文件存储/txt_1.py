import requests
from pyquery import PyQuery as pq

url = 'https://www.zhihu.com/explore'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}
html = requests.get(url, headers=headers).text
print(html)
doc = pq(html)
items = doc('.explore-tab .feed-item')
print(items)
with open('zhihu.txt', 'wb') as f:
    f.write(items)
