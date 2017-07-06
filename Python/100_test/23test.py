#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-28 13:35:56
# @Author  : jhb (jhbnanyou@163.com)
# @Link    : 
# @Version : $Id$

"""
  *
  ***
 *****
*******
 *****
  ***
   *

   注意：sys.stdout.write(obj + '\n')   = print obj
"""

from sys import stdout

for i in range(4):
	for j in range(3-i):
		stdout.write('')     #不换行打印
	for k in range(2*i+1):
		stdout.write('*')
	print

for i in range(3):
	for j in range(i+1):
		stdout.write('')
	for k in range(5-2*i):
		stdout.write('*')
	print



