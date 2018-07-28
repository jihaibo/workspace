# -*- coding:utf-8 -*-
author = 'haibo'
time = '2018-7-28'
"""
内置方法：__setitem__

简单地重定向到真正的字典 self.data
"""

class MySetitem:
    def __setitem__(self,key,value):
        print 'key = %s,value = %s' % (key,value)

mysetitem = MySetitem()
mysetitem['haibo'] = '90'
mysetitem['dingli'] = '80'
mysetitem['jianguang'] = '100'

