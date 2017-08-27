"""hellodjango URL Configuration

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
from django.conf.urls import include
# from app.views import welcome

# 列表 保存了所有由url() 函数生成的路由映射
urlpatterns = [
    # HELLODJANGO/app/urls文件
    url(r'^admin/', admin.site.urls),
    # url(r'^app/', welcome)    #使用如下的方式代替此种方式
    url(r'^app/', include('app.urls')),
    # url(r'^app/', include('app.urls'))    # url(r'', views.welcome),    
    
]

# from django.conf.urls import url
# from django.contrib import admin

# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
# ]