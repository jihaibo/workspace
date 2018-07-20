#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-05-09 14:15:06
# @Author  : jhb (jhbnanyou@163.com)
# @Link    : 
# @Version : 数据库连接配置

import MySQLdb
# print MySQLdb
try:
	conn = MySQLdb.Connect(
		host = '127.0.0.1',
		port = 3309,
		user = 'root',
		passwd = '123456',
		db = 'school',
		charset = 'utf8'
		)
	#获取游标
	cursor = conn.cursor()
	

	#创建表user
	sql_create = "create table if not exists user(userid int primary key auto_increment,username varchar(25))"
	#插入数据
	sql_insert = "insert into user(userid,username) values(1,'jihaibo')"
	#查询数据
	sql_select = "select * from user"
	#更新数据
	sql_update = "update user set username = 'hypo' where userid = 1"
	#删除数据
	sql_delete = "delete form user where userid = 1"



	try:

		#执行新建表语句
		cursor.execute(sql_create)
		
		#执行插入数据语句
		cursor.execute(sql_insert)
		print cursor.rowcount       #查看是否对数据行数

                 
		#执行出查询语句
		cursor.execute(sql_select)
		print cursor.rowcount    #查看是否对数据行数
		rs = cursor.fetchall()  #取出所有数据
		print rs
		for row in rs:
			print "userid = %s,username = %s" % row
		rs = cursor.fetchone()   #获取第一条数据



                  #执行更新语句
		cursor.execute(sql_update)
		rs = cursor.fetchall()
		print rs

                  #执行删除语句
		cursor.execute(sql_delete)

	except Exception as e:
		print e
		conn.rollback()     #出现异常后就回滚数据


finally:
	conn.commit()   #执行完语句后一定要提交一下事务，才能生效
	cursor.close()
	conn.close()