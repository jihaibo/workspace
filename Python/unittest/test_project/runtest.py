#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-03 16:37:23
# @Author  : jhb (jhbnanyou@163.com)
# @Link    : 
# @Version : $Id$
from HTMLTestRunner import HTMLTestRunner
import unittest
import time

test_dir  = "./"
discover = unittest.defaultTestLoader.discover(test_dir,pattern = "basemanage*.py")

if __name__ == '__main__':

	now = time.strftime("%Y-%m-%d %H_%M_%S")
	# 定义报告存放的路径、
	filename ='D:\\testpro\\report\\' + now + ' ' + 'result.html'
	fp = open(filename,'wb')
	#定义测试报告
	runner = HTMLTestRunner(stream=fp,title="测试报告",description='用例执行情况：')

	#runtest = unittest.TextTestRunner()
	#runtest.run(discover)   
	runner.run(discover)                              #运行测试用例

	fp.close()   #关闭报告文件


