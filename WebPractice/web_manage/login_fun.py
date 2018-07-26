# -*- coding:utf-8 -*-
author = 'haibo'
time = '2018-7-23'
"""
函数定义
"""

def login(username,passwd):
    if (username=='admin') and (passwd =='admin'):
        print "登录成功"
    else:
        print "登录失败"

user = raw_input("请输入用户名：")
pw = raw_input("请输入用户名密码:")
login(user,pw)
