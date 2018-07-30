# -*- coding:utf-8 -*-
author = 'haibo'
time = '2018-7-29'
"""
WSGI 学习第一篇
"""

class application:
    def __call__(self, environ, start_response):
        return ['xxx']
