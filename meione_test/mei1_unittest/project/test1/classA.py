# -*- coding: utf-8 -*-

from selenium import webdriver
import time

class ClassA(object):

    def open_baidu(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(6)
        driver.get("http://www.baidu.com")
        time.sleep(1)
        driver.quit()