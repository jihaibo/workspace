#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-03 14:22:46
# @Author  : jhb (jhbnanyou@163.com)
# @Link    : 
# @Version : $Id$ 
'''
discover()自动识别测试用例
'''

import unittest

#定义测试用例的目录为当前目录
test_dir = './'
discover = unittest.defaultTestLoader.discover(test_dir,pattern = 'basemanage*.py')

if __name__ == '__main__':
	runner = unittest.TextTestRunner()
	runner.run(discover)