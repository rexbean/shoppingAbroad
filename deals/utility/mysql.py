#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb


class PyMysql:
    def __init__(self,sql):
	self.sql = sql
	self.ip  = "140.82.4.24"
	self.user = "root"
	self.pwd  = "renchao"
	self.db   = "shopping"  

    def execute(self):
	db = MySQLdb.connect(self.ip,self.user,self.pwd,self.db,charset='utf8')
	cursor = db.cursor()
	try:
	    cursor.execute(self.sql)
	    db.commit()
	except e:
	    print "error" + e
	    db.rollback()
	db.close()

