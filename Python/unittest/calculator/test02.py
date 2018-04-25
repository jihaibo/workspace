#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-05-19 16:50:08
# @Author  : jhb (jhbnanyou@163.com)
# @Link    : 
# @Version : $Id$

from calculator import Count
import unittest

class TestCount(unittest.TestCase):

	def setUP(self):
		print ("basemanage start")

	def test_add(self):
		j = Count(2,3)
		self.assertEqual(j.add() , 5)

	def test_add2(self):
		j = Count(41 , 76)
		self.assertEqual(j.add(), 118,msg="输入的结果不相等118")

	def tearDOWN(self):
		print ("basemanage end")

if __name__ == '__main__':
	#构造测试集
	suite = unittest.TestSuite()
	suite.addTest(TestCount("test_add"))
	suite.addTest(TestCount("test_add2"))

	#执行测试集
	runner = unittest.TextTestRunner()
	runner.run(suite)

	


