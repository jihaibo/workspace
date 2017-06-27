#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-13 15:56:15
# @Author  : jhb (jhbnanyou@163.com)
# @Link    : 
# @Version : $Id$
from selenium import webdriver
import unittest
import os
import time
import login
import random

class MyTest(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome()
		self.driver.implicitly_wait(30)
		self.url = "https://saas.mei1.com"
		self.verificationErrors = []

	def test_add_customer(self):
		driver = self.driver
		driver.get(self.url)
                  #登录引用
		login.login(self)
		time.sleep(2)

                  #新增会员
		driver.find_element_by_partial_link_text('会员').click()
		time.sleep(1)
		driver.find_element_by_xpath('//*[@id="button_member_create"]/div').click()
		n =str(random.randint(1,500))
		name = "haibo" + n
		driver.find_element_by_id("input_member_name").send_keys(name)
		a =str(random.randint(1000,9999))
		b =str(random.randint(1000,9999))
		driver.find_element_by_id("input_member_mobile").send_keys("132"+ a + b)
		driver.find_element_by_id("select_member_source").click()
		driver.find_element_by_id("select_member_source_0").click()
		driver.find_element_by_id("select_member_store").click()
		driver.find_element_by_id("select_member_store_2").click()
		driver.find_element_by_id("button_member_new_save").click()
		time.sleep(2)

                  #编辑会员
		driver.find_element_by_xpath('//*[@id="route-outlet"]/section/div[1]/div[1]/md-card[1]/div[1]/div[5]/div/input').send_keys(name)
		driver.find_element_by_xpath('//*[@id="route-outlet"]/section/div[1]/div[1]/md-card[1]/div[1]/div[5]/div/i').click()
		driver.find_element_by_css_selector('[aria-owns="menu_container_1418"]').click()
		time.sleep(10)
		driver.find_element_by_xpath('//*[@id="menu_container_1367"]/md-menu-content/md-menu-item[1]/button/span').click()
		time.sleep(2)
		driver.find_element_by_id("button_member_new_save").click()

		#删除会员
		driver.find_element_by_xpath('//*[@id="route-outlet"]/section/div[1]/div[1]/md-card[1]/div[1]/div[5]/div/input').send_keys(name)
		driver.find_element_by_xpath('//*[@id="route-outlet"]/section/div[1]/div[1]/md-card[1]/div[1]/div[5]/div/i').click()
		driver.find_element_by_xpath('//*[@id="route-outlet"]/section/div[1]/div[1]/md-card[2]/div[3]/md-list/md-list-item/div/div[5]/md-menu/a').click()
		driver.find_element_by_xpath('//*[@id="menu_container_1367"]/md-menu-content/md-menu-item[4]/button').click()
		driver.find_element_by_xpath('/html/body/div[11]/md-dialog/md-dialog-actions/button[2]').click()

		#判断是否删除成功
		driver.find_element_by_xpath('//*[@id="route-outlet"]/section/div[1]/div[1]/md-card[1]/div[1]/div[5]/div/input').send_keys(name)
		driver.find_element_by_xpath('//*[@id="route-outlet"]/section/div[1]/div[1]/md-card[1]/div[1]/div[5]/div/i').click()
		text = driver.find_element_by_xpath('//*[@id="route-outlet"]/section/div[1]/div[1]/md-card[2]/div[3]/div/span[1]').getText()
		print text
		self.assertEqual(text,u"当前共搜到0条记录")
		time.sleep(2)
        

	def tearDown(self):
		self.driver.close()
		self.assertEqual([],self.verificationErrors)
if __name__ == '__main__':
	unittest.main()
