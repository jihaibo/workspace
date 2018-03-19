# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
	return HttpResponse(u"欢迎光临  Python学堂！")

def first(request):
	return render(request,'first.html')

def home(request):
	string = u"打印一串字符串到页面"
	return render(request,'string.html',{'string':string})


def second(request):
 	TutoriaList = ["HTML","CSS","jQuery","Django"]
 	return render(request,'second.html',{'TutoriaList':TutoriaList})
 	
def third(request):
	info_dict = {'site':u'百家讲坛','content':u'今夜有戏'}
	return render(request,'third.html',{'info_dict':info_dict})

def four(request):
	List = map(str,range(100) )#长度为100的List
	return render(request,'four.html',{'List':List})

