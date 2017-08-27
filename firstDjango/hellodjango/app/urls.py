from django.conf.urls import url    # 引入django.urls中的url函数，该函数负责django中所有的路由映射
from . import views 

# 列表 保存了所有由url() 函数生成的路由映射
urlpatterns = [
    url(r'', views.welcome),
    # url(r'^app/', include('app.urls')),   # HELLODJANGO/app/urls文件
    # url(r'^admin/', admin.site.urls)
]