#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-14 10:00:20
# @Author  : jhb (jhbnanyou@163.com)
# @Link    : 
# @Version : $Id$

'''
模仿静态变量的用法
'''

def varfunc():
	var = 0
	print 'var = %d' % var
	var += 1
if __name__ == '__main__':
	for i in range(3):
		varfunc()

#类的属性
#作为类的一个属性吧

class Static():
	StaticVar = 5
	def varfunc(self):
		self.StaticVar += 1
		print self.StaticVar

print Static.StaticVar
a = Static()
for i in range(3):
	a.varfunc()
