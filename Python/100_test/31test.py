#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-12 14:55:31
# @Author  : jhb (jhbnanyou@163.com)
# @Link    : 
# @Version : $Id$

'''
题目：请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。
'''
letter = raw_input("please input:")
if letter == 'S':
	print ('please input second letter:')
	letter = raw_input('please imput')
	
	if letter == 'a':
		print ('Saturday')
	elif letter == 'u':
		print ('Sunday')
	else:
		print ('day error')

elif letter == 'F':
	print 'Friday'

elif letter == 'M':
	print 'Monday'

elif letter =='T':
	print ('please input second letter')
	letter = raw_input('please input')

	if  letter == 'u':
		print 'Tuesday'
	elif letter =='h':
		print 'Thursday'
	else:
		print ('day error')

elif letter == 'W':
	print 'Wendesday'

else:
	print ('day error')