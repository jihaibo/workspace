#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-27 18:16:39
# @Author  : jhb (jhbnanyou@163.com)
# @Link    : 
# @Version : $Id$

'''
使用lambda来创建匿名函数。
'''
MAXIMUM = lambda x , y : ( x  > y )  * x + ( x < y ) * y
MINIUM = lambda x , y : (x > y)  * y + (x < y) * x

if __name__ == '__main__':
	a = 10
	b = 20 
	print 'The largar one is %d ' % MAXIMUM(a,b)
	print 'The lower one is %d ' % MINIUM(a,b)
