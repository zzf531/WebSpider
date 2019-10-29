# -*- coding:utf-8 -*-
import re


def change_scor(scor):
    if scor:
        return scor
    else:
        return '无法获取分数'


def change_publish(url):
    return re.sub('\s', '', url)


def change_price(url):
    if len(url) > 1:
        return url[1] + url[0]
    else:
        if '元' in url[0]:
            return url[0]
        else:
            return url[0] + '元'


def change_author(author):
    return re.sub('\s', '', author)


# title
def change_title(title):
    return re.sub('\s', '', title)


# ['18', 'August,', '2005']
def change_date(data):
    if type(data) == list and len(data) == 3:
        return str(data[0] + data[1] + data[2])
    else:
        return data
