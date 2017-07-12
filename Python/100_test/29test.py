#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-12 14:40:11
# @Author  : jhb (jhbnanyou@163.com)
# @Link    : 
# @Version : $Id$

'''
给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。
'''
s = int(raw_input('plese enter a num:\n'))
a = s / 10000
b = s % 10000 /1000
c = s % 1000 / 100
d = s % 100 / 10
e = s % 10

if a != 0:
	print "5 num:",e,d,c,b,a
elif b != 0:
	print "4 nunm:",e,d,c,b
elif b != 0:
	print "3 nunm:",e,d,c
elif b != 0:
	print "2 nunm:",e,d
elif b != 0:
	print "1 nunm:",e