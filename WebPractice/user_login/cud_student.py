# -*- coding: utf-8 -*-
'''
调用数据库中的cud方法
'''
from sql_studnet import *

hypo = Mysqlhelper(user='root',passwd='123456',db='student')

name = raw_input('请输入用户名：')
passwd = raw_input('请输入用户名密码：')

# 添加用户
params = [name,passwd]
sql = 'insert users (name,passwd) values(%s,%s)'
# 这里不用再单独调用open和close，因为他们已经封装到cud函数里面了
hypo.cud(sql,params)


