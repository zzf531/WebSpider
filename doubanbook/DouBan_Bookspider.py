# -*- coding:utf-8-*-
import requests
from bs4 import BeautifulSoup
from doubanbook.DouBan_url import channel
from doubanbook.change import change_scor, change_publish, change_author, change_price, change_title, change_date
import time
import re
import pymysql
import random


def main(url):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text.encode("utf-8"), "lxml")
    tag = url.split("?")[0].split("/")[-1]
    detils = soup.select("#subject_list > ul > li > div.info > div.pub")
    scors = soup.select("#subject_list > ul > li > div.info > div.star.clearfix > span.rating_nums")
    persons = soup.select("#subject_list > ul > li > div.info > div.star.clearfix > span.pl")
    titles = soup.select("#subject_list > ul > li > div.info > h2 > a")
    for detil, scor, person, title in zip(detils, scors, persons, titles):
        all = detil.get_text().split("/")
        l = []
        try:
            if len(all) == 4:
                title = change_title(title.get_text().split(':')[0])
                author = change_author(detil.get_text().split("/", 4)[0])
                translators = "没有翻译"  # 翻译
                publish = change_publish(detil.get_text().split("/")[1])  # 出版社
                date = change_date(detil.get_text().split("/")[2].split())
                price = change_price(detil.get_text().split("/")[3].split())
                scor = change_scor(scor.get_text().split())  # 评分
                number = person.get_text().split()
            elif len(all) == 6:
                title = change_title(title.get_text().split(':')[0])
                author = change_author(detil.get_text().split("/", 4)[0])
                translators = detil.get_text().split("/", 4)[1]  # 翻译
                publish = change_publish(detil.get_text().split("/")[3])  # 出版社
                date = change_date(detil.get_text().split("/")[4].split())
                price = change_price(detil.get_text().split("/")[5].split())
                scor = change_scor(scor.get_text().split())  # 评分
                number = person.get_text().split()
            else:
                title = change_title(title.get_text().split(':')[0])
                author = change_author(detil.get_text().split("/", 4)[0])
                translators = detil.get_text().split("/", 4)[1]  # 翻译
                publish = change_publish(detil.get_text().split("/")[2])  # 出版社
                date = detil.get_text().split("/")[3]
                price = change_price(detil.get_text().split("/")[4].split())
                scor = change_scor(scor.get_text().split())  # 评分
                number = person.get_text().split()

            print(tag, title, author, translators, publish, date, price, scor, number)
            l.append([tag, title, author, translators, publish, date, price, scor, number])
            print(type(date))

            # 将爬取的数据依次填入列表中
            sql = "INSERT INTO allbooks values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"  # 这是一条sql插入语句
            cur.executemany(sql, l)  # 执行sql语句，并用executemary()函数批量插入数据库中
            conn.commit()  # 主函数到此结束

        except IndexError:
            print('资料不全，无法爬去')
            continue


# 将Python连接到MySQL中的python数据库中
conn = pymysql.connect(user="root", password="", database="test_url", charset='utf8')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS allbooks')  # 如果数据库中有allbooks的数据库则删除
sql = """CREATE TABLE allbooks(      
        tag CHAR(255) NOT NULL,
        title CHAR (255) NOT  NULL,  
        author CHAR(255),      
        translators CHAR(255),     
        publish CHAR(255),     
        date CHAR(255),    
        price CHAR(255),     
        sco CHAR(255),         
        number CHAR(255)       
 )"""
cur.execute(sql)  # 执行sql语句，新建一个allbooks的数据库

# start = time.clock()  # 设置一个时钟，这样我们就能知道我们爬取了多长时间了
# main('https://book.douban.com/tag/古典文学')  # 执行主函数，开始爬取
# print('https://book.douban.com/tag/科技')  # 输出要爬取的链接，这样我们就能知道爬到哪了，发生错误也好处理
# time.sleep(int(format(random.randint(0, 9))))  # 设置一个随机数时间，每爬一个网页可以随机的停一段时间，防止IP被封
# end = time.clock()
# print('Time Usage:', end - start)  # 爬取结束，输出爬取时间
count = cur.execute('select * from allbooks')
print('has %s record' % count)  # 输出爬取的总数目条数


for urls in channel.split():
    urlss = [urls + "?start={}&type=T".format(str(i)) for i in range(0, 980, 20)]
    for url in urlss:
        main(url)


# 释放数据连接
if cur:
    cur.close()
if conn:
    conn.close()
