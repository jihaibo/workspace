# -*- coding: utf-8 -*-

import time
from selenium import webdriver
from logger import Logger

mylogger = Logger(logger='TestMyLog').getlog()
class TestMyLog(object):

    def print_log(self):
        driver = webdriver.Chrome()
        mylogger.info(u"打开浏览器")
        driver.maximize_window()
        mylogger.info(u"最大化浏览器窗口。")
        driver.implicitly_wait(8)

        driver.get("https://www.baidu.com")
        mylogger.info(u"打开百度首页")
        time.sleep(1)
        mylogger.info(u"暂停一秒")
        driver.quit()
        mylogger.info(u"关闭退出浏览器")

testlog = TestMyLog()
testlog.print_log()