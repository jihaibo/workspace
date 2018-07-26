# -*- coding: utf-8 -*-

import MySQLdb
from hashlib import sha1
from sql_studnet import *

#接收用户输入
name = raw_input('请输入用户名：')
pwd = raw_input('请输入用户密码：')

"""
#对密码加密
m = sha1()
m.update(pwd.encode('utf-8'))
pwd2 = m.hexdigest()

"""

#根据用户名查询密码
sql = 'select passwd from users where name = %s'
hypo = Mysqlhelper(user='root',passwd='123456',db='student')
result = hypo.see_all(sql,[name])
if result == ():
    print ('用户名错误！')
elif result[0][0] == pwd:
    print ('登录成功！')
else:
    print ('密码错误！')

print result




























