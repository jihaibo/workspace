#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-12 16:30:59
# @Author  : jhb (jhbnanyou@163.com)
# @Link    : 
# @Version : $Id$

'''
题目：将一个数组逆序输出。
程序分析：用第一个与最后一个交换。
'''

if __name__ == '__main__':
	a = [9,6,5,4,1]
	N = len(a)
	print a 
	for i in range(len(a)/2):
		a[i],a[N-i-1] = a[N-i-1],a[i]
	print a
