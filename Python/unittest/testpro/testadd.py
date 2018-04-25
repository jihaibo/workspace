#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-03 14:02:53
# @Author  : jhb (jhbnanyou@163.com)
# @Link    : 
# @Version : $Id$

from calculator import Count
import unittest

class TestAdd(unittest.TestCase):

	def setUp(self):
		print ("basemanage case start")

	def tearDown(self):
		print ("basemanage case end")

	def test_add(self):
		j = Count(2,3)
		self.assertEqual(j.add(),5)

	def test_add2(self):
		j = Count(41,76)
		self.assertEqual(j.add(),117)

if __name__ == '__main__':
	unittest.main()