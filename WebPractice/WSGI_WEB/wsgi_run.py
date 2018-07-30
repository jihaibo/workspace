# -*- coding:utf-8 -*-
author = 'haibo'
time = '2018-7-29'
"""
WSGI 学习第一篇
"""

def run(application):
    environ = {}

    def start_response(xxx):
        pass
    result = application(environ,start_response)
    def write(data):
        pass
    for data in result:
        write(data)





















