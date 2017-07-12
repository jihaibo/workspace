#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-12 15:28:04
# @Author  : jhb (jhbnanyou@163.com)
# @Link    : 
# @Version : $Id$

'''
文本颜色设置
'''

class bcolors:
	HEADER = '\033[95m'
	OKBLUE  = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FALL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'
print bcolors.WARNING + 'waring color?' + bcolors.ENDC
