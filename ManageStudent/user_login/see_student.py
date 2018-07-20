# -*- coding:utf-8 -*-
'''
查询所有用户信息
'''
from sql_studnet import *
hypo = Mysqlhelper(user='root',passwd='123456',db='student')
sql = 'select * from users'
hypo.see_all(sql)
