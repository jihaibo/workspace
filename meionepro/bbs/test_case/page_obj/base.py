# -*- coding: utf-8 -*-
# _author = jhb
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Page(object):
    '''
    页面基础类，用于所有页面的继承
    '''

    base_url = 'https://saas.mei1.com'

    def __init__(self, selenium_driver, base_url=base_url, parent=None):
        self.base_url = base_url
        self.driver = selenium_driver
        self.timeout = 10
        self.parent = parent



    def _open(self,url):
        url = self.base_url + url
        self.driver.get(url)
        assert self.on_page(),'Did not land on %s' % url

    def open(self):
        self._open(self.url)

    def on_page(self):
        return self.driver.current_url.encode('utf-8') ==(self.base_url + self.url)

    def find_element(self,*loc):
        return self.driver.find_element(*loc)

    def find_elements(self,*loc):
        return self.driver.find_elements(*loc)

    def script(self,src):
        return self.driver.execute_script(src)

    def swtich_frame(self,loc):
        return self.driver.swith_to_frame(loc)

    def send_keys(self,loc,value,clear_first = True,click_first= True):
        try:

            # getattr相当于self.loc
            loc = getattr(self, "_%s" % loc)
            if click_first:
                self.find_element(*loc).click()
            if clear_first:
                self.find_element(*loc).clear()
                self.find_element(*loc).send_keys(value)
        except ArithmeticError:
            print u"%s 页面中未能找到 %s 元素" % (self, loc)







