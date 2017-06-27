#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-02 17:29:37
# @Author  : jhb (jhbnanyou@163.com)
# @Link    : 
# @Version : $Id$

#计数器
class Count():

	def __init__(self,a,b):
		self.a = int(a)
		self.b = int(b)

	#计算加法
	def add(self):
		return self.a + self.b

	#计算减法
	def sub(self):
		return self.a - self.b

