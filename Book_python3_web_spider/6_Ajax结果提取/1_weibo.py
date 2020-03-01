from urllib.parse import urlencode
import requests
base_url = 'https://m.weibo.cn/api/container/getIndex?'

headers = {
    'Host': 'm.weibo.cn',
    'Referer': 'https://m.weibo.cn/u/2870450862',  # 刘昊然
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
    'X-Requested-With': 'XMLHttpRequest',
}

def get_page(since_id):
    params = {
        'type': 'uid',
        'value': '2870450862',  # 2870450862  2830678474
        'containerid': '1076032870450862',  # 1076032870450862  1076032830678474
    }
    if since_id != 0:
        params['since_id'] = since_id  # 字典运算
    url = base_url + urlencode(params)
    print(url)
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError as e:
        print('Error', e.args)

from pyquery import PyQuery as pq

def parse_page(json):
    if json:
        items = json.get('data').get('cards')
        for item in items:
            item = item.get('mblog')
            if item == None:
                continue
            else:
                weibo = {}
                # weibo['id'] = item.get('id')
                weibo['text'] = pq(item.get('text')).text()
                weibo['created_at'] = item.get('created_at')
                # weibo['attitudes'] = item.get('attitudes_count')
                # # weibo['comments'] = item.get('comments_count')
                # # weibo['reposts'] = item.get('reposts_count')
                yield weibo


if __name__ == '__main__':
    since_id = 0
    for page in range(1,99):
        json = get_page(since_id)
        since_id = json.get('data').get('cardlistInfo').get('since_id')
        results = parse_page(json)
        for result in results:
            print(result)
            with open('test.txt', 'a', encoding='utf-8') as f:
                f.write('时间 :' + result['created_at'] + '  内容 :' + result['text'] + '\n')
