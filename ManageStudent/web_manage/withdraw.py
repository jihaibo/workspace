# -*- coding:utf-8 -*-
author = 'haibo'
time = '2018-7-24'
"""
自动取款机打印凭证
"""

print "欢迎使用通协路交通银行取款机！"
car = raw_input("请输入您的卡号：")
passwd = raw_input("请输入您的密码：")
print "登录成功！进入取款业务。"
name = raw_input("请输入您的用户名：")
money = int(raw_input("请输入您的取款金额："))
print "正在交易中，请稍后......\n交易成功，请查收您的客户凭条！"
print "【交通银行自动取款机客户凭条】\n============================"
print "%s您好！\n您的卡号：%s\n本次交易金额为：%d\n欢迎下次使用！"%(name,car,money)
print "============================"