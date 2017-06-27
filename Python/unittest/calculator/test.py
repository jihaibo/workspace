#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-05-19 15:56:39
# @Author  : jhb (jhbnanyou@163.com)
# @Link    : 
# @Version : $Id$

from calculator import Count

#测试两个整数相加
class TestCount:

	def test_add(self):
		try:
			j = Count(2,3)
			add = j.add()
			assert(add == 5),'Integer addition result error!'
		except AssertionError as msg:
			print (msg)
		else:
			print ('Test Pass')

mytest = TestCount()
mytest.test_add()
