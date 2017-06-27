#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-02 16:54:33
# @Author  : jhb (jhbnanyou@163.com)
# @Link    : 	
# @Version : $Id$

import unittest

class Test(unittest.TestCase):
	
	def setUp(self):
		number = raw_input("Enter a number")
		self.number = int(number)

	def test_case(self):
		self.assertEqual(self.number,10,msg="Your input is not 10!")

	def tearDown(self):
		pass

if __name__ == '__main__':
	unittest.main()


