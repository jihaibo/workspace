#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-03 16:33:07
# @Author  : jhb (jhbnanyou@163.com)
# @Link    : 
# @Version : $Id$

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
	'''有道搜索测试'''

	def setUp(self):
		chromedriver ="C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
		os.environ["webdriver.chrome.driver"] = chromedriver
		self.driver = webdriver.Chrome(chromedriver)
		self.driver.implicitly_wait(10)
		self.base_url = "http://youdao.com"
		self.driver.maximize_window()

	def test_youdao(self):
		''' 有道搜索'''
		driver = self.driver
		driver.get(self.base_url + "/")
		driver.find_element_by_id("translateContent").clear()
		driver.find_element_by_id("translateContent").send_keys("webdriver")
		driver.find_element_by_id("qb").click()
		time.sleep(2)
		title  = driver.title
		self.assertEqual(title,"webdriver - 有道搜索")

	def tearDown(self):
		self.driver.close()

if __name__ == '__main__':
	unittest.main()





