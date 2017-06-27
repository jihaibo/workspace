#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-02 17:28:11
# @Author  : jhb (jhbnanyou@163.com)
# @Link    : 
# @Version : $Id$

"""
封装自己测试类
"""
from calculator import Count
import unittest

class Mytest(unittest.TestCase):

	 def setUp(self):
	 	print ("start")

	 def tearDown(self):
	 	print ("end")

class TestAdd(Mytest):

	def test_add(self):
		j = Count(2,3)
		self.assertEqual(j.add(),5)

	def test_add2(self):
		j = Count(41,76)
		self.assertEqual(j.add(),117)

class TestSub(Mytest):

	def test_sub(self):
		j = Count(2,3)
		self.assertEqual(j.sub(),-1)

	def test_sub2(self):
		j = Count(71,46)
		self.assertEqual(j.sub(),25)

if __name__ == '__main__':
	unittest.main()