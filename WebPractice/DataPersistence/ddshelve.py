# -*- coding:utf-8 -*-
author = 'haibo'
time = '2018-7-28'
"""
数据持久化

dbhash 只支持字符串类型的值
shelve 返回的字典值，支持：字符串、数字、元祖以及列表
"""

import shelve
db = shelve.open('mydb','c')
db['hypo'] = ['hypo','18721527961','shanghai','myworld',4000]
db['dingli'] = ['dingli','18000253621','shanghai','myworld',5000]
db['jianguang'] = ['jianguang','13774242580','nanjing','myworld',2000]
#print db

for k,v in db.iteritems():
    print k,':',v
db.close()
