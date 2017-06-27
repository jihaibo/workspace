#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-09 13:37:54
# @Author  : jhb (jhbnanyou@163.com)
# @Link    : 
# @Version : $Id$

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart

# 发送邮件服务器
smtpserver =  'smtp.163.com'
# 发送邮件用户/密码
user = 'jhbnanyou@163.com'
password = 'jhb104674'
# 发送邮箱
sender = 'jhbnanyou@163.com'
# 接受邮箱
receiver = 'haibo.ji@mei1.com'

# 发送邮件主题
subject = 'Python email test'

# 发送邮件附件
sendfile = open('D:\\testpro\\report\\log.txt','rb').read()
att = MIMEText(sendfile,'base64','utf-8')
att["Content-Type"] = 'application/octet-stream'
att["Content-Disposition"] = 'attachment;filename = "log.txt" '

# 编写 HTML 类型的邮件正文
msgRoot = MIMEMultipart('related')
msgRoot['Subject'] = subject
msgRoot.attach(att)

msg = MIMEText('<html><h1>你好!</h1></html>','html','utf-8')
msg['Subject'] = Header(subject , 'utf-8')
msg['from'] = 'jhbnanyou@163.com'
msg['to'] = 'haibo.ji@mei1.com'


#连接发送邮件
smtp = smtplib.SMTP()
smtp.connect(smtpserver)
smtp.login(user,password)
smtp.sendmail(sender , receiver , msg.as_string(),msgRoot.as_string())
smtp.quit()