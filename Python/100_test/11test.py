#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-23 10:28:42
# @Author  : jhb (jhbnanyou@163.com)
# @Link    : 
# @Version : $Id$

"""
题目：有一对兔子，从出生后第3个月起每个月都生一对兔子，
小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？
"""
def rabbit(n):
	a ,b = 1,1
	for i in range(n-1):
		a,b=b,a+b
	return a

print rabbit(22)
