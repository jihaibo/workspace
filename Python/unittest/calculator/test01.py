#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-05-19 16:07:02
# @Author  : jhb (jhbnanyou@163.com)
# @Link    : 
# @Version : $Id$
from calculator import Count
import unittest

class TestCount(unittest.TestCase):

	def setUP(self):
		print ("test start")

	def test_add(self):
		j = Count(2,3)
		self.assertEqual(j.add(),5)

	def tearDOWN(self):
		print ("test end")

if __name__ == '__main__':
	unittest.main()    #main()方法使用TestLoader类搜索所有包含在该模块中以‘’test‘’命名的测试方法，并自动执行他们

