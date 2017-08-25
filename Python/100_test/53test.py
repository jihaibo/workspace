#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-28 15:38:25
# @Author  : jhb (jhbnanyou@163.com)
# @Link    : 
# @Version : $Id$

'''
学习使用按位异或 ^ 。
程序分析：0^0=0; 0^1=1; 1^0=1; 1^1=0
'''
if __name__ == '__main__':
	a = 077
	b = a ^ 3
	print 'The a ^ 3 = %d' % b 
	b ^= 7
	print 'The a ^ b = %d' % b 