#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-22 15:19:54
# @Author  : jhb (jhbnanyou@163.com)
# @Link    : 
# @Version : $Id$

"""
斐波那契数列

分析：斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。
在数学上，费波那契数列是以递归的方法来定义

F(0) = 0     (n=0)
F(1)= 1    (n=1)
F(n) = F[n-1]+ F[n-2](n=>2)
"""
def fib(n):
	a,b =1,1
	for i in range(n-1):
		a,b=b,b+a
	return a
print fib(0)


