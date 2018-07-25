# -*- coding: utf-8 -*-
import  MySQLdb

while True:
    while True:
        user = raw_input('请输入用户名：')
        passwd = raw_input('请输入密码：')

        if passwd == 'jhb104674':
            print ('*********学生查询系统**********')
            print ('1.学生类型信息')
            print ('*******************************')
            break
        else:
            print ('--请重新输入密码--')
    num = int(raw_input('请输入功能相对的数字：'))
    print ()

    conn =MySQLdb.connect(
        host = '127.0.0.1',
		port = 3309,
		user = 'root',
		passwd = '123456',
		db = 'student',
		charset = 'utf8'
    )
    cursor = conn.cursor()
    if num ==1:
        sql = 'select id,name from users'
        cursor.execute(sql)
        results = cursor.fetchall()
        print ('学生序号    学生姓名')
        for row in results:
            print (row)
    print ('********结束了*********')
    break




