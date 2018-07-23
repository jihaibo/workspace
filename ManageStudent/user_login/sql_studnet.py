# -*- coding: utf-8 -*-
'''
封装SQL语句参数化
'''

import MySQLdb

class Mysqlhelper:

    # 初始化参数
    def __init__(self,user,passwd,db,host='127.0.0.1',port=3309,charset='utf8'):
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd
        self.db = db
        self.charset = charset

    # 连接数据库
    def open(self):
        self.conn = MySQLdb.connect(
            host = self.host,
            port = self.port,
            db = self.db,
            user = self.user,
            passwd = self.passwd,
            charset = self.charset
        )
        self.cursor = self.conn.cursor()

    # 关闭数据库
    def close(self):
        self.cursor.close()
        self.conn.close()

    # 增删改
    def cud(self,sql,params):
        try:
            self.open()

            self.cursor.execute(sql,params)
            self.conn.commit()
            print ('操作成功！')
            self.close()
        except Exception as e:
            print e

    # 查询获取多个值
    def see_all(self,sql,params=()):
        try:
            self.open()

            self.cursor.execute(sql,params)
            result = self.cursor.fetchall()

            self.close()
            return result
        except Exception as e:
            print e.message





































