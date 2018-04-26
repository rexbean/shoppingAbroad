
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
        print(self.params)
	response = requests.post(self.requrl,data = self.params,headers = self.header) 
	return response

# getReq = PyRequest("http://140.82.4.24:7001","/testGet",{})
# r = getReq.doGet()
# print r.cookies['csrfToken']

# data = {"title":"title..","link":"link..","picture":"picture...","hotness":"hotness..","editor":"good","posttime":"2018","description":"description..","price":"123.45","shipping":"123123"}
# postReq = PyRequest("http://140.82.4.24:7001","/scrapy/dealnews/add",data)
# r = postReq.doPost()
# print r.text
#print r.cookies['csrfToken']

# npostReq = PyRequest("http://140.82.4.24:7001","/scrapy/dealnews/add"+"?_csrf="+r.cookies['csrfToken'],data)
# nr = npostReq.doPost()
# print nr.text
# print nr.cookies['csrfToken']

