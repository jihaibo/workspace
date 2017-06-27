#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-03 14:15:09
# @Author  : jhb (jhbnanyou@163.com)
# @Link    : 
# @Version : $Id$
'''
没有集合套件，手动添加测试用例
'''

import unittest

#加载测试文件
import testadd
import testsub

#构造测试集
suite  = unittest.TestSuite()

suite.addTest(testadd.TestAdd("test_add"))
suite.addTest(testadd.TestAdd("test_add2"))

suite.addTest(testsub.TestSub("test_sub"))
suite.addTest(testsub.TestSub("test_sub2"))

if __name__ == '__main__':
	#执行测试
	runner = unittest.TextTestRunner()
	runner.run(suite)
