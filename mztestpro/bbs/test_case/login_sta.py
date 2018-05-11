# -*- coding: utf-8 -*-
from time import sleep
import unittest,random,sys
sys.path.append("./models")
sys.path.append("./page_obj")
from models import myunit,function
from page_obj.loginPage import login

class loginTest(myunit.MyTest):
    """
    登录测试

    """

    #测试用户登录
    def user_login_verify(self,username="",password=""):
        login(self.driver).user_login(username,password)

    def test_login1(self):
        """
        用户名为空，密码为空登录
        :return:
        """
        self.user_login_verify()
        po = login(self.driver)
        self.assertEqual(po.login_error_hint(),u"请输入用户名")
        function.insert_img(self.driver,"user_empty.jpg")

    def test_login2(self):
        """
        用户账号或密码错误
        :return:
        """
        self.user_login_verify(username="18721527961",password="12345678")
        po = login(self.driver)
        self.assertEqual(po.login_error_hint(),u"用户名或密码错误")
        function.insert_img(self.driver,"user_error.jpg")

    def test_login3(self):
        """
        用户名与密码输入正确，登录成功
        :return:
        """
        self.user_login_verify(username="18721527961",password="jhb104674")
        sleep(2)
        po = login(self.driver)
        self.assertEqual(po.login_success(),u"美问")
        function.insert_img(self.driver,"suer_success.jpg")

if __name__ =="__main__":
    unittest.main()

