#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-23 16:49:56
# @Author  : jhb (jhbnanyou@163.com)
# @Link    : 
# @Version : $Id$

'''
题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
程序分析：利用while语句,条件为输入的字符不为'\n'。
'''
import string

s = raw_input('imput s string:\n')
lettrts = 0
space = 0
digit = 0
others = 0

for c in s:
	if c.isalpha():
		lettrts +=1
	elif c.isspace():
		space +=1
	elif c.isdigit():
		digit +=1
	else:
		others +=1

print 'char = %d,space = %d , digit = %d , other = %d ' % (lettrts,space,digit,others)