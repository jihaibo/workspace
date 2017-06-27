# -*- coding: utf-8 -*-
# @Date    : 2017-06-09 17:00:07
# @Author  : jhb (jhbnanyou@163.com)
# @Link    : 
# @Version : $Id$
from HTMLTestRunner import HTMLTestRunner 
from email.mime.text import MIMEText
from email.header import Header
import smtplib
import unittest
import time
import os


import sys
reload(sys)
sys.setdefaultencoding('utf8')

# ======================定义发送邮件==========================
def send_mail(file_new):
	f = open(file_new,'rb')
	mail_body = f.read()
	f.close()

	msg = MIMEText(mail_body,'html','utf-8')
	msg['Subject'] = Header("自动化测试报告",'utf-8')
	msg['from'] = 'jhbnanyou@163.com'
	msg['to'] = 'haibo.ji@mei1.com'

	smtp = smtplib.SMTP()
	smtp.connect("smtp.163.com")
	smtp.login("jhbnanyou@163.com","jhb104674")
	smtp.sendmail("jhbnanyou@163.com","haibo.ji@mei1.com",msg.as_string())
	smtp.quit()
	print("email has send out  !")

# ===========查找测试报告目录，找到最新生成的测试报告==========
def new_report(testreport):
	lists = os.listdir(testreport)
	lists.sort(key = lambda fn: os.path.getmtime(testreport + "\\" + fn))
	file_new = os.path.join(testreport,lists[-1])
	return file_new

if __name__ == '__main__':
	test_dir = "./"
	test_report = "./report"

	discover = unittest.defaultTestLoader.discover(test_dir,pattern='test_*.py')
	now =time.strftime("%Y-%m-%d_%H_%M_%S")
	filename = test_report + '\\' + now + 'result.html'
	fp = open(filename,'wb')
	runner = HTMLTestRunner(stream = fp , title = '测试报告', description = '用例执行情况：')

	runner.run(discover)
	fp.close()
	new_report = new_report(test_report)
	send_mail(new_report)    #发送测试报告













	 