# -*- coding:utf-8 -*-
author = 'haibo'
time = '2018-7-23'
"""
用户注册功能

说明：isdigit() 检测字符串是否只由数字组成
"""

def registerUsr():
    # 请输入用户名称
    username = raw_input('请输入您的名称：')
    # 判断用户名长度
    if (len(username)>=3 and len(username)<=20):
        idcard = raw_input('请输入您的账号：')
        # 判断账号是否为数字
        if (idcard.isdigit()):
            phone = raw_input('请输入您的手机号：')
            # 判断手机号的格式以及长度
            if (phone.isdigit() and len(phone) >=7 and len(phone) <=11):
                print "注册成功！"
            else:
                print "您输入的手机格式错误"
        else:
            print "账号格式不正确，请输入数字！"

    else:
        print "用户名称的长度必要在3—20之间"


registerUsr()




















