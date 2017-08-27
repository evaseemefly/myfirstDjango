from cmdb import views
from django.conf.urls import url,include
from django.contrib import admin

# url(r'^login/', views.login),
    # url(r'^cmdb/index/', views.index),

urlpatterns = [
    url(r'^login/', views.login,name='login'),
    url(r'^index/', views.index),
    url(r"^user_info/",views.user_info),
    url(r'^userdetail-(?P<uid>\d+)/',views.userdetail),
    url(r'^userdel-(?P<uid>\d+)/',views.userdel),

]