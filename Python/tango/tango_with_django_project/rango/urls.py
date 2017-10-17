#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-08-30 14:56:17
# @Author  : jhb (jhbnanyou@163.com)
# @Link    : 
# @Version : $Id$

from django.conf.urls import patterns,url
from rango import views

urlpatterns = patterns('',
	url(r'^$',views.index,name = 'index'))