
#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys
import requests
import json

class PyRequest():
    def __init__(self,url,addr,params):
        self.requrl  = url + addr
	self.params  = params
	self.header  = {"Connection":"keep-alive","content-type":"text/plain;charset=utf-8"}
    
    def doGet(self):
	response = requests.get(self.requrl,data = json.dumps(self.params),headers = self.header)
	return response
	
    def doPost(self):
	print("-------------------------------------")
        print(json.dumps(self.params))
	print("-------------------------------------")
	response = requests.post(self.requrl,data = json.dumps(self.params),headers = self.header) 
	return response

# getReq = PyRequest("http://140.82.4.24:7001","/testGet",{})
# r = getReq.doGet()
# print r.cookies['csrfToken']
jsondata = {"picture": "https://dealnews.a.ssl.fastly.net/images/spacer.png", "link": "https://www.dealnews.com/lw/click.html?20,2,17288762", "editor": "false", "title": "Under Armour Men's UA Storm Jacket", "price": "$30", "hotness": " 0", "posttime": "2018-04-26T03:13:20-04:00", "shipping": "free shipping", "description": " Proozy Outlet via eBay offers the Under Armour Men's UA Storm Lightweight Waterproof Jacket in several colors (Navy Soldier pictured) for $29.99 with free shipping . That's tied with our mention from a week ago and the best deal we could find by $12. It's available in sizes S to L."}
response = requests.post("http://140.82.4.24:7001/scrapy/dealnews/add",data = jsondata)
print response.text
# data = {"title":"title..","link":"link..","picture":"picture...","hotness":"hotness..","editor":"good","posttime":"2018","description":"description..","price":"123.45","shipping":"123123"}
# postReq = PyRequest("http://140.82.4.24:7001","/scrapy/dealnews/add",data)
# r = postReq.doPost()
# print r.text
#print r.cookies['csrfToken']

# npostReq = PyRequest("http://140.82.4.24:7001","/scrapy/dealnews/add"+"?_csrf="+r.cookies['csrfToken'],data)
# nr = npostReq.doPost()
# print nr.text
# print nr.cookies['csrfToken']

