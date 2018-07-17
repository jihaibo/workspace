# -*- coding: utf-8 -*-
from time import sleep
import unittest,sys
sys.path.append("./models")
sys.path.append("./page_obj")
from models import myunit,function
from page_obj.loginPage import login
# from page_obj.coustomPage import

class coustomTest(myunit.MyTest):
    '''
    客户测试
    '''

    #用户登录
    def test_login(self,username='18721527961',password='jhb104674'):
        login(self.driver).user_comm_login(username,password)
        print "success"

if __name__=='__mian__':
    unittest.main()
