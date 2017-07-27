#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-27 15:42:31
# @Author  : jhb (jhbnanyou@163.com)
# @Link    : 
# @Version : $Id$

'''
求输入数字的平方，如果平方运算后小于 50 则退出。
'''
TRUE = 1
FALSE = 0
def SQ(x):
	return x*x
print 'if result<50,exit()'
again = 1
while  again:
	num = int(raw_input('please enter a num:'))
	print 'result:%d' % (SQ(num))
	if SQ(num) >50:
		again = TRUE
	else:
		again = FALSE