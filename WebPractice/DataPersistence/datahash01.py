# -*- coding:utf-8 -*-
author = 'haibo'
time = '2018-7-28'
"""
数据持久化
"""

import dbhash
db = dbhash.open('tem','c')
db['西施'] = '西施浣纱'
db['貂蝉'] = '貂蝉拜月'
db['昭君'] = '昭君出塞'

print '--------------没有进行任何操作的数据---------------'
for k,v in db.items():
    print k,v
if db.has_key('西施'):
    del db['西施']
print '------------删除键为‘西施’对应的数据---------------'
for k,v in db.items():
    print k,v
db.close()













