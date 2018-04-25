# -*- coding:utf-8 -*-

from selenium import webdriver
import re
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(6)

driver.get("http://home.baidu.com/contact.html")
# 获取页面源码
doc = driver.page_source
# 利用正则，找出 xxx@xxx.xxx 的字段，保存到emails列表
emails = re.findall(r'[\w]+@[\w\.-]+',doc)

for email in emails:
    print (email)

time.sleep(2)

#获取浏览器版本
print (driver.capabilities['version'])

#获取当前页面url
print (driver.current_url)

#获取当前页面title
print (driver.title)

#截图保存
driver.get_screenshot_as_file("D:\\meione_test\\mei1_unittest\\project\\lianxi\\baidu.png")

#设置浏览器大小
driver.set_window_size(1024,768)
time.sleep(2)
driver.quit()