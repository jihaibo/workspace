# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup

url = 'http://www.itest.info/courses'
soup = BeautifulSoup(requests.get(url).text,'html.parser')

for course in soup.find_all('h4'):
    print (course.text)
