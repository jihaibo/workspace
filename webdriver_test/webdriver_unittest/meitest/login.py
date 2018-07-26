# -*- coding: utf-8 -*-

import unittest
from selenium import webdriver
import time

class MeiOne(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome()
        self.driver.get("http://saas.basemanage.mei1.info")
        self.driver.maximize_window()
        self.driver.implicitly_wait(2)


    def test_meione_Login(self):

        driver = self.driver
        driver.find_element_by_id("userName").send_keys("18721527961")
        driver.find_element_by_id("password").send_keys("jhb104674")
        driver.find_element_by_id("loginBtn").click()
        time.sleep(2)
        driver.find_element_by_id("eid_2").click()
        driver.find_element_by_id("employeeLoginBtn").click()
        time.sleep(15)

        #刷新当前页面
        driver.refresh()

        time.sleep(3)

    def tearDown(self):

        title = self.driver.title

        # 获取当前页面链接
        url1 = self.driver.current_url

        #获取指定文本信息
        ele_string = self.driver.find_element_by_xpath('/html/body/div[5]/div[1]/div[2]/md-list/md-list-item[1]/div/a/span/span').text
        if (title == u'美问'):
            print "与预期结果一致"

        print ele_string
        print url1

        #获取浏览器版本
        print (self.driver.capabilities['version'])

        #当前页面进行截图
        self.driver.get_screenshot_as_file("D:\\webdriver_test\\image\\meione.png")

        self.driver.quit()

if __name__ == '__main__':
    unittest.main()


