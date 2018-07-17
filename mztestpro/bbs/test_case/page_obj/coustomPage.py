# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By
from base import Page
from time import sleep

class custom(Page):
    '''
    客户页面元素
    '''

    #会员导航栏定位
    custom_navigation_loc = (By.XPATH,'/html/body/div[5]/div[1]/div[2]/md-list/md-list-item[7]/div/a/span/span')
    #新增按钮定位
    custom_add_button_loc = (By.XPATH,'//*[@id="button_member_create"]/div')
    #客户姓名定位
    custom_clientName_loc = (By.ID,'input_member_name')


