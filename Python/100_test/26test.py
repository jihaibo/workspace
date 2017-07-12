#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-12 14:19:38
# @Author  : jhb (jhbnanyou@163.com)
# @Link    : 
# @Version : $Id$

'''
利用递归方法求5!。
'''
def fact(j) :
	sum = 0
	if j == 0:
		sum = 1
	else:
		sum = j * fact(j-1)
	return sum

for i in range(5):
	print '%d! = %d ' % (i,fact(i))