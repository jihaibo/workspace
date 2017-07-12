#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-07-12 16:18:23
# @Author  : jhb (jhbnanyou@163.com)
# @Link    : 
# @Version : $Id$

'''
求一个3*3矩阵对角线元素之和
程序分析：利用双重for循环控制输入二维数组，再将a[i][i]累加后输出。
'''

if __name__ == '__main__':
	a = []
	sum = 0.0
	for i in range(3):
		a.append([])
		for j in range(3):
			a[i].append(float(raw_input('input num:\n')))
	for i in range(3):
		sum += a[i][i]
	print sum