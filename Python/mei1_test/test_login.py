# -*- coding: utf-8 -*-
# @Date    : 2017-06-13 15:00:06
# @Author  : jhb (jhbnanyou@163.com)
# @Link    : 
# @Version : $Id$
'''
login自动化测试
'''
from selenium import webdriver
import unittest
import time
import os

class MyTest(unittest.TestCase):

	def setUp(self):
		chromedriver = "C:\Users\Haibo\AppData\Local\Google\Chrome\Application\chromedriver.exe"
		os.environ["webdriver.chrome.driver"] = chromedriver
		self.driver = webdriver.Chrome(chromedriver)
		self.driver.implicitly_wait(30)
		self.url = "https://saas.mei1.com"
		self.driver.maximize_window()

	def test_login(self):
		''' 登录测试'''
		driver = self.driver
		driver.get(self.url + '/')
		driver.find_element_by_id("userName").clear()
		driver.find_element_by_id("userName").send_keys("18721527961")
		driver.find_element_by_id("password").clear()
		driver.find_element_by_id("password").send_keys("jhb104674")
		driver.find_element_by_id("loginBtn").click()
		time.sleep(2)
		driver.find_element_by_id("eid_0").click()
		driver.find_element_by_id("employeeLoginBtn").click()
		time.sleep(2)
		title  = driver.title
		print title
		self.assertEqual(title,u'美问')
		driver.find_element_by_partial_link_text('会员').click()
		time.sleep(20)


	def tearDown(self):
		self.driver.close()
if __name__ == '__main__':
	unittest.main()






