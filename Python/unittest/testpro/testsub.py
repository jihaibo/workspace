#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-03 14:08:19
# @Author  : jhb (jhbnanyou@163.com)
# @Link    : 
# @Version : $Id$
from calculator import Count
import unittest

class TestSub(unittest.TestCase):

	def setUp(self):
		print ("basemanage case start")
	def tearDown(self):
		print ("basemanage case end")

	def test_sub(self):
		j = Count(2,3)
		self.assertEqual(j.sub(),-1)

	def test_sub2(self):
		j = Count(71,46)
		self.assertEqual(j.sub(),25)

if __name__ == '__main__':
	unittest.main()