# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup

url = 'https://www.v2ex.com/'
res = requests.get(url)
#res.encoding = 'gb18030'
soup = BeautifulSoup(res.text,'html.parser')

for span in soup.find_all('span',class_='item_hot_topic_title'):
    print (span.find('a').text.decode('unicode_escape'),span.find('a')['href'])

'''
python3的解决办法：字符串.encode('utf-8').decode('unicode_escape')

python2：字符串.decode('unicode_escape')

'''
