from django.shortcuts import *  
from django.http import HttpResponse  
from blog.models import BlogsPost
from blog.views import *

# Create your views here.
def myBlogs(request):
	blog_list =BlogPost.objects.all()  
        return render_to_response('BlogTemplate.html', {'blog_list':blog_list})