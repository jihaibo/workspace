#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-28 15:34:36
# @Author  : jhb (jhbnanyou@163.com)
# @Link    : 
# @Version : $Id$

'''
题目：学习使用按位或 | 。
程序分析：0|0=0; 0|1=1; 1|0=1; 1|1=1
'''
if __name__ == '__main__':
	a = 077
	b = a | 3
	print 'a | b = %d' % b
	b |= 7
	print 'a | b = %d' % b 