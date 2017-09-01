"""myweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from myfirstapp.views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    url(r'^admin/', admin.site.urls),    
    url(r'^$',index),
    url(r'^nextpage/$',nxt),
    url(r'^detail/(\d+)$',detail),
    url(r'^delete/(\d+)$',delete_record),
    url(r'^myform/$',form),
    url(r'^blog/$',comment),
    url(r'^deletepost/(\d+)',deletePost),
    url(r'^search/$',search),
    url(r'^register/$',register_user),
    url(r'^auth_check/$',check,name='check'),
    url(r'^logout/$',logout),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
