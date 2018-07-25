# -*- coding: utf-8 -*-
'''
爬虫第一讲
'''
import requests

url = 'https://ke.qq.com/agency/index/index.html#tab=showCoupon'
html = requests.get(url).text
print (html)