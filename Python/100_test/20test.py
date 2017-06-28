#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-27 16:41:37
# @Author  : jhb (jhbnanyou@163.com)
# @Link    : 
# @Version : $Id$

"""
球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，
求它在第10次落地时，共经过多少米？第10次反弹多高？
"""
tour = []
height = []
n = int(raw_input("please enter count:\n "))

hei = 100.0  #起始高度
for i in range(1,n+1):
	# 从第二次开始，落地时的距离应该是反弹高度乘以2（弹到最高点再落下）
	if i ==1:
		tour.append(hei)
	else:
		tour.append(2*hei)
	hei /=2
	height.append(hei)
print('total: tour = {0}'.format(sum(tour)))
print('high:height = {0}'.format(height[-1]))	
