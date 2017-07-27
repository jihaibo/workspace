#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-27 15:48:38
# @Author  : jhb (jhbnanyou@163.com)
# @Link    : 
# @Version : $Id$

'''
两个变量值互换。
'''

def exchange(a,b):
	a,b = b,a
	return (a,b)

if __name__ == '__main__':
	x = 10
	y = 20
	print 'start: x = %d,y = %d' % (x,y)
	x,y = exchange(x,y)
	print 'result: x = %d,y = %d' % (x,y)
