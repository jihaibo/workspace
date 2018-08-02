# -*- coding:utf-8 -*-
author = 'haibo'
time = '2018-8-1'
"""
服務器端的構建

構建一個小型服务器
"""
import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  # 生成socket對象
host = socket.gethostname()                           # 獲取服務器名稱
port = 1234
#s.bind((host,port))                                   # 綁定socket地址
s.connect((host,port))
print s.recv(1024)
s.close()