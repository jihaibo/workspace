# -*- coding: utf-8 -*-

from selenium import webdriver
import time


driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(6)
driver.get("http://news.baidu.com")
time.sleep(1)

for image in driver.find_elements_by_tag_name("img"):
    print (image.text)
    print (image.size)
    print (image.tag_name)

time.sleep(4)
driver.quit()
