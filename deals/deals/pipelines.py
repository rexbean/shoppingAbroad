# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


import pymysql
from deals import settings

class DBPipeline(object):
    def __init__(self):
        # connect to database
        try:
            self.connect = pymysql.connect(
                host=settings.MYSQL_HOST,
                db=settings.MYSQL_DBNAME,
                user=settings.MYSQL_USER,
                passwd=settings.MYSQL_PASSWD,
                charset='utf8',
                use_unicode=True)
            # cursor is used to do the operation of database
            print('DB has been connected')
            self.cursor = self.connect.cursor();
        except Exception as e:
            print(e)

    def process_item(self, item, spider):
        try:
            # insert data
            self.cursor.execute(
                """insert into M_dealnews(title, link, picture, hotness, editor_recommond, posttime, description, price, shipping)
                value (%s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                (item['title'],
                 item['link'],
                 item['pic'],
                 item['hotness'],
                 item['editor'],
                 item['postTime'],
                 item['description'],
                 item['price'],
                 item['shipping']))

            # commit
            self.connect.commit()
        except Exception as error:
            # print error
            print(error)
        return item
