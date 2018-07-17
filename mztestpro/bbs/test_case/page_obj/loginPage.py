# -*- coding: utf-8 -*-
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from base import Page
from time import sleep

class login(Page):
    """
    用户登录页面
    """
    url = '/'

    #登录用户名定位
    login_username_loc = (By.ID,'userName')
    #登录密码定位
    login_password_loc = (By.ID,'password')
    #登录按钮定位
    login_button_loc = (By.ID,'loginBtn')
    #登录角色选择
    login_selectEmployee_loc = (By.ID,'eid_1')
    #登录门店进入
    login_finalButton_locc = (By.ID,'employeeLoginBtn')
    #登录失败提示
    login_error_hint_loc =(By.ID,'id_alert_text')
    #登录成功验证
    #login_success_loc = (By.ID,'employeeLoginBtn')


    #登录用户名
    def login_username(self,username):
        self.find_element(*self.login_username_loc).send_keys(username)

    #登录密码
    def login_password(self,password):
        self.find_element(*self.login_password_loc).send_keys(password)

    #登录按钮
    def login_button(self):
        self.find_element(*self.login_button_loc).click()

    #选择角色
    def login_selsctEmployee(self):
        self.find_element(*self.login_selectEmployee_loc).click()

    #进入门店
    def login_finalButton(self):
        self.find_element(*self.login_finalButton_locc).click()

    #登录测试
    def user_login(self,username ="18721527961",password="jhb104674"):
        """
        获取的用户名登录密码
        :param username:
        :param password:
        :return:
        """
        self.open()
        self.login_username(username)
        self.login_password(password)
        self.login_button()
        #self.login_selsctEmployee()
        #self.login_finalButton()
        sleep(1)

    #用户密码或者账号错误
    def login_error_hint(self):
        return self.find_element(*self.login_error_hint_loc).text

    #用户登录成功
    def login_success(self):
        return self.driver.title


    #统一登录入口
    def user_comm_login(self,username="18721527961",password='jhb104674'):
        """
        用户登录入口（用户名、密码）
        :param username:
        :param password:
        :return:
        """
        self.open()
        self.login_username(username)
        self.login_password(password)
        self.login_button()
        sleep(1)
        self.login_selsctEmployee()
        self.login_finalButton()
        sleep(3)







