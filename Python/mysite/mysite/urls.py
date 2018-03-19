from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','learn.views.index'),
#    url(r'^add/$','calc.views.add', name = 'add') ,
#    url(r'^add/(\d+)/(\d+)/$','calc.views.add2',name = 'add2'),
    url(r'^home','calc.views.index',name = 'home'),
    url(r'^first','learn.views.first',name='first'),
    url(r'^string','learn.views.home',name = 'string'),
    url(r'^second','learn.views.second',name = 'second'),
    url(r'^third','learn.views.third',name = 'third'),
    url(r'^four','learn.views.four',name = 'four'),
    url(r'^add/$','former.views.add',name ='add'),
)
