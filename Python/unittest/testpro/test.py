#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-03 15:01:19
# @Author  : jhb (jhbnanyou@163.com)
# @Link    : 
# @Version : $Id$
"""
1、跳过测试和预期失败
2、可以用在测试类上
3、可以用在具体的测试案例
"""
import unittest

class Mytest(unittest.TestCase):

	def setUp(self):
		pass

	def tearDown(self):
		pass

	@unittest.skip("直接跳过")
	def test_skip(self):
		print "basemanage aaa"

	@unittest.skipIf(3 > 2,"当条件为True时跳过")
	def test_skip_if(self):
		print "basemanage bbb"

	@unittest.skipUnless(3 > 2,"当条件为True时执行测试")
	def test_skip_unless(self):
		print ("basemanage ccc")

	@unittest.expectedFailure           # 测试标记为失败。不管执行结果是否失败，统一标记为失败
	def test_expected_failure(self):
		assertEqual(2,3)


if __name__ == '__main__':
	unittest.main()
