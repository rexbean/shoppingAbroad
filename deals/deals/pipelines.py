# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DBPipeline(object):
    def __init__(self):
        # 连接数据库
        self.connect = pymysql.connect(
            host=settings.MYSQL_HOST,
            db=settings.MYSQL_DBNAME,
            user=settings.MYSQL_USER,
            passwd=settings.MYSQL_PASSWD,
            charset='utf8',
            use_unicode=True)
            # 通过cursor执行增删查改
        self.cursor = self.connect.cursor();

    def process_item(self, item, spider):
        try:
            # 插入数据
            self.cursor.execute(
                """insert into M_dealnews(title, link, picture, hotness, editor_recommond, posttime, description, price, shipping)
                value (%s, %s, %s, %s, %s, %s)""",
                (item['title'],
                 item['link'],
                 item['pic'],
                 item['hotness'],
                 item['editor_recommond'],
                 item['postTime'],
                 item['description'],
                 item['price'],
                 item['shipping']))

            # 提交sql语句
            self.connect.commit()

        except Exception as error:
            # 出现错误时打印错误日志
            log(error)
        return item
