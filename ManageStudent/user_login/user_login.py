# -*- coding: utf-8 -*-
import MySQLdb

user_list = []
conn = MySQLdb.connect(
    host = '127.0.0.1',
    port = 3309,
    user = 'root',
    passwd = '123456',
    db = 'student',
    charset = 'utf8'
)
cursor = conn.cursor()
'''
sql = 'select name,passwd from users'
cursor.execute(sql)
result = cursor.fetchall()
for user in result:
    #将所有的用户给到user大列表
    user_list.append(user)

#获取user中所有的name
i = 0
name_list =[]
while i < len(user_list):
    name_list.append(user_list[i][0])
    i+=1


def login():
    name = raw_input("please enter name:")
    passwd = raw_input("please enter password:")
    while name not in name_list:
        name = raw_input('please enter right name:')
        passwd = raw_input('请输入密码：')
    index = name_list.index(name,0,len(name_list))
    if passwd == user_list[index][1]:
        print ('登录成功!')
    else:
        print ('输入密码错误，登录失败！')

'''
def login01():
    name = raw_input('请输入用户名：')
    passwd = raw_input('请输入密码：')
    sql = 'select passwd from users where name = %s'
    cursor.execute(sql,[name])
    result = cursor.fetchall()
    if result ==():
        print ('用户名不存在!')
    elif result[0][0] ==passwd:
        print ('恭喜您登录成功！')
    else:
        print ('您输入的密码错误!')


while True:
    print ('**********登录**********')
    print ('1.登录')
    print ('0.退出系统')
    print ('************************')

    num = int(raw_input('请输入您的选择:'))
    while num not in range(0,2):
        num = int(raw_input('输入的选择错误，请重输入:'))
    if num ==1:
        login01()
    else:
        print ('程序结束!')
        break