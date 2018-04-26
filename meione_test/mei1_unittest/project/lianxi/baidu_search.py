# -*- coding:utf-8 -*-

import time

'''
import imp
basepage = imp.load_source('basepage','D:/workspace/meione_test/mei1_unittest/project/basemanage/basepage.py')
import basepage
'''

import sys
sys.path.append('D:/workspace/meione_test/mei1_unittest/project/')
from basemanage.basepage import BasePage

from selenium import webdriver




class BaiduSearch(object):

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)

    basepage = BasePage(driver)

    def open_baidu(self):
        self.basepage.open_url("https://www.baidu.com")
        time.sleep(1)

    def test_search(self):
        self.driver.find_element_by_id('kw').send_keys("Selenium")
        time.sleep(1)
        self.basepage.back()
        self.basepage.forward()
        self.basepage.quit_browser()

baidu = BaiduSearch()
baidu.open_baidu()
baidu.test_search()