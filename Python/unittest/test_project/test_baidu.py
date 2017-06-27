#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-03 15:47:29
# @Author  : jhb (jhbnanyou@163.com)
# @Link    : 
# @Version : $Id$

from selenium import webdriver
import unittest
import time
import os

class MyTest(unittest.TestCase):
	'''百度搜索测试'''

	def setUp(self):
		chromedriver ="C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
		os.environ["webdriver.chrome.driver"] = chromedriver
		self.driver = webdriver.Chrome(chromedriver)
		self.driver.implicitly_wait(10)
		self.base_url = "http://baidu.com"
		self.driver.maximize_window()

	def test_baidu(self):
		'''查询测试'''
		driver = self.driver
		driver.get(self.base_url + "/")
		driver.find_element_by_id("kw").clear()
		driver.find_element_by_id("kw").send_keys("unittest")
		driver.find_element_by_id("su").click()
		time.sleep(2)
		title  = driver.title
		self.assertEqual(title,"unittest_百度搜索")

	def tearDown(self):
		self.driver.quit()

if __name__ == '__main__':
	unittest.main()





