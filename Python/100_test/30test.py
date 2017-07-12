#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-12 14:49:11
# @Author  : jhb (jhbnanyou@163.com)
# @Link    : 
# @Version : $Id$

'''
题目：一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。
'''
a = int(raw_input('please enter a num:\n'))
x = str(a)
flag = True

for i in  range (len(x)/2):
	if x[i] != x[-i-1]:
		flag = False
		break
if flag:
	print '%d is a huiwenshu!' % a
else:
	print '%d is not a huiwenshu' % a

