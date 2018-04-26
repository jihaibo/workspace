# -*- coding: utf-8 -*-
import os
import time
from selenium.common.exceptions import NoSuchElementException

class BasePage(object):
    """
    主要是把常用的几个Selenium方法封装到BasePage这个类，我们这里演示以下几个方法
    back()
    forward()
    get()
    quit()
    """

    def __init__(self,driver):
        '''
        写一个构造函数，有一个参数driver
        :param driver:
        '''
        self.driver = driver

    def back(self):
        """
        浏览器后退
        :param none:
        """
        self.driver.back()

    def forward(self):
        """
        浏览器前进按钮
        :param none:
        """
        self.driver.forward()

    def open_url(self,url):
        """
        打开url站点
        :param url:
        """
        self.driver.get(url)

    def quit_browser(self):
        """
        关闭浏览器
        :return:
        """
        self.driver.quit()

    #隐性等待
    def wait(self,seconds):
        self.driver.implicitly_wait(seconds)

    def get_windows_img(self):
        """
        截图保存在根目录Screenhots文件夹下
        :return:
        """
        file_path = os.path.dirname(os.getcwd())+'/basemanage/Screenshots/'
        rq = time.strftime('%Y.%m.%d %H%M',time.localtime())
        screen_name =file_path + rq + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)

        except Exception as e:
            print "出现异常"


    #定位元素
    def find_element(self,selector):
        """
        这个地方为什么是根据=>来切割字符串，请看页面里定位元素的方法
         submit_btn = "id=>su"
         login_lnk = "xpath => //*[@id='u1']/a[7]"  # 百度首页登录链接定位
         如果采用等号，结果很多xpath表达式中包含一个=，这样会造成切割不准确，影响元素定位
        :param selector:
        :return:
        """
        element = ''
        if '=>' not in selector:
            return self.driver.find_element_by_id(selector)
        selector_by = selector.split('=>')[0]
        selector_value = selector.split('=>')[1]

        if selector_by == "i" or selector_by == 'id':
            try:
                element = selector.driver.find_element_by_id(selector_value)
            except NoSuchElementException as e:
                print ('fail')
        elif selector_by =='n' or selector_by =='name':
            element = selector.driver.find_element_by_name(selector_value)
        elif selector_by == "c" or selector_by == 'class_name':
            element = self.driver.find_element_by_class_name(selector_value)
        elif selector_by == "l" or selector_by == 'link_text':
            element = self.driver.find_element_by_link_text(selector_value)
        elif selector_by == "p" or selector_by == 'partial_link_text':
            element = self.driver.find_element_by_partial_link_text(selector_value)
        elif selector_by == "t" or selector_by == 'tag_name':
            element = self.driver.find_element_by_tag_name(selector_value)
        elif selector_by == "x" or selector_by == 'xpath':
            try:
                element = self.driver.find_element_by_xpath(selector_value)
            except NoSuchElementException as e:
                print ('fail')
        elif selector_by =='s' or selector_by == 'selector_selector':
            element = self.driver.find_element_by_css_selector(selector_value)
        else:
            raise NameError("please enter a valid type of targeting element.")
        return element

    #输入
    def type(self,selector,text):

        el = self.find_element(selector)
        el.clearn()
        try:
            el.send_keys(text)
            print ('pass')
        except NameError as e:
            print ("Faild to type in input box with %s" % e)
            self.get_windows_img()

    #清除文本
    def clear(self, selector):

        el = self.find_element(selector)
        try:
            el.clear()
            print ("Clear text in input box before typing.")
        except NameError as e:
            print ("Failed to clear in input box with %s" % e)
            self.get_windows_img()

    # 点击元素
    def click(self, selector):

        el = self.find_element(selector)
        try:
            el.click()
            print ("The element \' %s \' was clicked." % el.text)
        except NameError as e:
            print ("Failed to click the element with %s" % e)

    # 或者网页标题
    def get_page_title(self):
        print ("Current page title is %s" % self.driver.title)
        return self.driver.title

    @staticmethod
    def sleep(seconds):
        time.sleep(seconds)
        print ("Sleep for %d seconds" % seconds)


