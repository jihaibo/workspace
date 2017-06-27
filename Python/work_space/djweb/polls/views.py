from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	return HttpResponse("Hello World! You are at the poll index")
def detail(req,poll_id):
	return HttpResponse("You are looking at pool %s. " %poll_id)
def results(req,poll_id):
	return HttpResponse("You are looking at the results of poll %s ." %poll_id)
def vote(req,poll_id):
	return HttpResponse("You are voting on poll %s" %poll_id)