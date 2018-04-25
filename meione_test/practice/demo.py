# -*- coding: utf-8 -*-

import time
from selenium import webdriver

class MeiOne(object):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)

    def open_meione(self):
        self.driver.get("http://saas.basemanage.mei1.info")
        self.driver.maximize_window()
        time.sleep(1)

    def test_login(self):
        self.driver.find_element_by_id("userName").send_keys("18721527961")
        self.driver.find_element_by_id("password").send_keys("jhb104674")
        self.driver.find_element_by_id("loginBtn").click()
        time.sleep(1)
        self.driver.find_element_by_id("eid_2").click()
        self.driver.find_element_by_id("employeeLoginBtn").click()
        time.sleep(5)
        title_string = self.driver.title
        try:
            assert u'美问' in title_string
            print ('Test pass.')
        except Exception as e:
            print ('basemanage fail')

    def refresh(self):
        self.driver.refresh()
        time.sleep(4)


    def close(self):
        self.driver.quit()

meionetest =MeiOne()
meionetest.open_meione()
meionetest.test_login()
meionetest.close()