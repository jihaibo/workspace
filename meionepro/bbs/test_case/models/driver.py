# -*- coding: utf-8 -*-

from selenium.webdriver import Remote
from selenium import webdriver

#启动浏览器驱动
def browser():
    driver = webdriver.Chrome()
    return driver

if __name__ == '__main__':
    dr = browser()
    dr.get("https://saas.mei1.com")
    dr.quit()

