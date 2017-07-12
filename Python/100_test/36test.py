#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-12 15:34:50
# @Author  : jhb (jhbnanyou@163.com)
# @Link    : 
# @Version : $Id$

'''
求一百以内的素数
'''
lower = int(raw_input('lower between:'))
upper = int(raw_input('upper between:'))

for num in range(lower,upper+1):
	if num >1:
		for i in range(2,num):
			if (num % i ) == 0:
				break
		else:
			print num