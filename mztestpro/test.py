# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import os

if 'HTTP_PROXY' in os.environ:del os.environ['HTTP_PROXY']

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(8)

url = 'https://saas.mei1.com/'
driver.get(url)
driver.find_element_by_id("userName").send_keys("18721527961")
driver.find_element_by_id("password").send_keys("jhb104674")
driver.find_element_by_id("loginBtn").click()
sleep(1)
driver.find_element_by_id("eid_1").click()
driver.find_element_by_id("employeeLoginBtn").click()
sleep(5)

#driver.add_cookie({'name':'key-aaaaaa','value':'value-bbbbb'})

'''
for cookie in driver.get_cookies():
    print "%s->%s" % (cookie['name'],cookie['value'])
'''
cookie = driver.get_cookies()
print cookie

sleep(2)
driver.quit()
