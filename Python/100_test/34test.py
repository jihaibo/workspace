#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-12 15:24:02
# @Author  : jhb (jhbnanyou@163.com)
# @Link    : 
# @Version : $Id$

'''
练习函数调用。
'''
def hello_world():
	print 'hello world'

def three_hellos():
	for i in range(3):
		hello_world()

if __name__ == '__main__':
	three_hellos()