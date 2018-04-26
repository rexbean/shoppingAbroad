# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GoodsItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()      # 标题 字符串
    link = scrapy.Field()       # 站内连接 字符串
    pic = scrapy.Field()        # 图片链接 （没来及转base64） 字符串
    hotness = scrapy.Field()    # 关注热度 字符串
    editor = scrapy.Field()     # 编辑者推荐 boolean
    postTime = scrapy.Field()   # 发布时间（未解析） 字符串
    description = scrapy.Field()# 商品描述 字符串
    price = scrapy.Field()      # 价格信息 字符串
    shipping = scrapy.Field()   # 运费 字符串


class BlogItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    pic = scrapy.Field()
    hot = scrapy.Field()
    editor = scrapy.Field()
