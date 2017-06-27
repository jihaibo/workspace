#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-22 15:01:14
# @Author  : jhb (jhbnanyou@163.com)
# @Link    : 
# @Version : $Id$

"""
输入三个整数x,y,z，请把这三个数由小到大输出
"""
a = int(raw_input('first num: \n'))
b = int(raw_input('second num: \n'))
c = int(raw_input('third num: \n'))

l = sorted([a,b,c])
print 'the num is: %d,%d,%d' %(l[0],l[1],l[2])


m =[]
for i in range(3):
	x = int(raw_input('enter number: \n'))
	m.append(x)
m.sort()
print m