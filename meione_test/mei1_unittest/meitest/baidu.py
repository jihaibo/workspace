# -*- coding: utf-8 -*-

from selenium import webdriver
import time
import os

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.maximize_window()

driver.find_element_by_id("kw").send_keys("Selenium2")
driver.find_element_by_id("su").click()
time.sleep(5)

driver.quit()