# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render,redirect

from west.models import Character

from django import forms

from django.core.context_processors import csrf

from django.contrib.auth.decorators import login_required

from django.contrib.auth.decorators import user_passes_test

from django.contrib.auth.forms import UserCreationForm


def first_page(request):
	return HttpResponse("<p>西餐</p>")


def staff(request):
	staff_list = Character.objects.all()
	return render(request, 'templay.html', {'staffs': staff_list})

def templay(request):
	context = {}
	context['label'] = 'Hello World!'
	return render(request,'templay.html',context)

#get请求
def form(request):
	return render(request,'form.html')

def inverstigate(request):
	rlt = request.GET['staff']
	return HttpResponse(rlt)

'''
#post请求
def investigate(request):
	ctx = {}
	ctx.update(csrf(request))
	if request.POST:
		ctx['rlt'] = request.POST['staff']
	return render(request,"investigate.html",ctx)
'''

#post请求的数存入数据库
class CharacterForm(forms.Form):
	name = forms.CharField(max_length = 200)

def investigate(request):
	if request.POST:
		form = CharacterForm(request.POST)
		if form.is_valid():
			submitted = form.cleaned_data['name']
			new_recode = Character(name = submitted)
			new_recode.save()

	form = CharacterForm()
	ctx = { }
	ctx.update(csrf(request))
	all_records = Character.objects.all()
	ctx['staff'] = all_records
	ctx['form']  = form 
	return render(request,"investigate.html",ctx)


def user_login(request):
	'''
            login
	'''
	if request.POST:
		username = password = ' '
		username = request.POST.get('username')
		password = request.POST.get('password')
		user          = authenticate(username = username,password = password)
		if user is not None and user.is_active:
			login(request,user)
			return render('/')

	ctx  =  { }
	ctx.update(csrf(request))
	return render(request,'login.html',ctx)


def user_logout(request):
	'''
	logout
	URL:/users/logout

	'''
	logout(request)
	return redirect('/')


def diff_response(request):
	if request.user.is_authenticated():
		content = "<p> my dear user </p>"
	else:
		content = "<p>you wired stanger</p>"
	return HttpResponse(content)

@login_required         #login_required，它是Django预设的装饰器。user_only()的回复结果只能被登录用户看到，而未登录用户将被引导到其他页面。
def user_only(request):
	return HttpResponse("<p>This message is for logged in user only.</p>")


'''
装饰器带有一个参数，该参数是一个函数对象name_check。当name_check返回真值，即用户名为vamei时，specific_user的结果才能被用户看到。
'''
def name_check(user):   
	return user.get_username() == 'vamei'

@user_passes_test(name_check)
def specific_user(request):
	return HttpResponse("<p>for Vamei only</p>")


def register(request):
	if request.method == 'POST':
		form  = UserCreationForm(request.POST)
		if form.is_valid():
			new_user = form.save()
		return redirect('/')
	else:
		form = UserCreationForm()
		ctx = {'form': form}
		ctx.update(csrf(request))
		return render(request,"register.html",ctx)

		