#!/usr/bin/python
# -*- coding:utf-8 -*-
import scrapy
import subprocess
import sys

if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8')

from scrapy.selector import Selector
from scrapy.http import HtmlResponse
from deals.items import GoodsItem
from utility.utility import Utility
from utility.request import PyRequest 

class dealNewsSpider(scrapy.Spider):    

    name = "dealNews"
    urls = []

    start_urls = [
        # search the account with keyword
        "https://www.dealnews.com/"

    ]

    def parse(self, response):

        r = self.executeJS()


        #parseHot(r)

        #parseBlog(r)

        self.parseGoods(r)

    def executeJS(self):
        url = "https://www.dealnews.com/"
        print('executing JS in '+url+'...')
        cmd = "phantomjs ./deals/getBody.js '%s'" % url
        print "cmd is",cmd

        stdout, stderr =  subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr = subprocess.PIPE).communicate()
        print(stderr)
        r = HtmlResponse(url=url, body=stdout)

        return r

    def parseHot(self, r):
        for i in range(1,12):
            goodsItem = GoodsItem()

            rootPath        = '//div[@class="carousel-slider"]/div['+str(i)+']/div[1]'
            titlePath       = './a[2]/div'
            pricePath       = './span//text()'
            restWordPath    = './a[2]/div/text()[2]'
            linkPath        = './a[2]/@href'
            picPath         = './a[2]/span/@data-bg-src'
            editorPath      = './div[2]'

            print('======================='+str(i)+'============================')
            root = r.xpath(rootPath)

            # this is title
            title   = root.xpath(titlePath+'//text()').extract_first().strip('\n').strip()
            # this is link
            link    = root.xpath(linkPath).extract_first()
            # this is pic
            # need convert to base64
            pic     = root.xpath(picPath).extract_first()

            # this is for price
            if len(root.xpath(titlePath).xpath(pricePath)) != 0:
                title += ' '+root.xpath(titlePath).xpath(pricePath).extract_first().strip('\n').strip()
            # this is for the rest words
            if len(root.xpath(restWordPath)) != 0:
                title += ' ' + root.xpath(restWordPath).extract_first().strip('\n').strip()

            # this is for the editor choice
            if len(root.xpath(editorPath)) != 0:
                editor = True
            else:
                editor = False

            goodsItem['title'] = title
            goodsItem['link'] = link
            goodsItem['pic'] = pic
            goodsItem['hot'] = 5
            goodsItem['editor'] = editor

            yield goodsItem

    def parseGoods(self,r):

        index = 0
        rootPath = '//*[@id="page-body"]/div/div/div/div[4]/div/div'
        for selector in r.xpath(rootPath):
            goodsItem = GoodsItem()
            discription = ''

            titlePath   = './div[2]/div/h3/a//text()'
            pTimePath   = './div[2]/div/div/time/@datetime'
            picPath     = './div[1]/div/a[2]/img/@src'
            linkPath    = './div[2]/div/a/@href'
            dPath       = './div[3]/div//text()'
            hotnessPath = './div[2]/div/div[@class="hotness info"]/img/@alt'
            pricePath   = './div[2]/div/div[@class="content-call-out"]'
            shipPath    = './small[@class ="content-sub-call-out"]//text()'
            editorPath  = './div[1]/div[@title= "Editor\'s Choice"]//text()'



            title           = selector.xpath(titlePath).extract_first()
            publishedTime   = selector.xpath(pTimePath).extract_first()
            pic             = selector.xpath(picPath).extract_first()
            discriptionList = selector.xpath(dPath).extract()
            link            = selector.xpath(linkPath).extract_first()

            price           = selector.xpath(pricePath+'//text()').extract_first()
            shipping        = selector.xpath(pricePath).xpath(shipPath).extract_first()

            hotness = '0'
            # for hotnewss, someone doesn't have
            if len(selector.xpath(hotnessPath)) != 0:
                hotness = selector.xpath(hotnessPath).extract_first().split(':')[1].split('/')[0]

            if len(selector.xpath(editorPath)) != 0:
                print(True)
                editor = True
            else:
                editor = False

            discription = Utility.concatenateList(discriptionList)


            if title is not None:

                print('=================='+str(index)+'=====================')
                goodsItem['title'] = title
                goodsItem['postTime'] = publishedTime
                goodsItem['pic'] = pic
                goodsItem['discription'] = discription
                goodsItem['link'] = link
                goodsItem['hotness'] = hotness
                goodsItem['editor'] = editor
                if price is not None:
                    price = price.strip('\n').strip()
                    goodsItem['price'] = price
                else:
                    goodsItem['price'] = '$-1'
                if shipping is not None:
                    goodsItem['shipping'] = shipping
                else:
                    goodsItem['shipping'] = ''

                #print(goodsItem)
		
		data = {'title':goodsItem['title'],'link':goodsItem['link'],'picture':goodsItem['pic'],'hotness':goodsItem['hotness'],'editor':goodsItem['editor'],'posttime':goodsItem['postTime'],'description':goodsItem['discription'],'price':goodsItem['price'],'shipping':goodsItem['shipping']}
		print data
		postReq = PyRequest("http://140.82.4.24:7001","/scrapy/dealnews/add",data)
		re = postReq.doPost()
		print re.text
		# print postReq.doPost().text
                index+=1
