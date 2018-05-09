# -*- coding: utf-8 -*-

from selenium.webdriver import Remote
from selenium import webdriver

#启动浏览器驱动
def browser():
    driver = webdriver.Chrome()
    host = '127.0.0.1:8080' #运行本机
    dc = {'browserName':'chrome'} #指定浏览器
    driver = Remote(command_executor=)
