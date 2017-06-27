# -*- coding: utf-8 -*-
# @Date    : 2017-06-13 15:00:06
# @Author  : jhb (jhbnanyou@163.com)
# @Link    : 
# @Version : $Id$

#=============================封装登录方法============================

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import unittest
import time

def login(self):
	driver = self.driver
	driver.maximize_window()
	driver.find_element_by_id("userName").clear()
	driver.find_element_by_id("userName").send_keys("18721527961")
	driver.find_element_by_id("password").clear()
	driver.find_element_by_id("password").send_keys("jhb104674")
	driver.find_element_by_id("loginBtn").click()
	time.sleep(1)
	driver.find_element_by_id("eid_0").click()
	driver.find_element_by_id("employeeLoginBtn").click()
	time.sleep(3)














