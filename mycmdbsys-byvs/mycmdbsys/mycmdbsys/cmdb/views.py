from django.shortcuts import render,HttpResponse,redirect
# from django.shortcuts import HttpResponse
from cmdb import models
# Create your views here.

def login(request):
    if request.method=="GET":
        return render(request,'login.html')
    elif request.method=="POST":
        # 获取前台提交过来的用户名与密码
        u=request.POST.get('user')
        p=request.POST.get('pwd')

        obj=models.UserInfo.objects.filter(username=u,pwd=p).first()
        if obj:
            return redirect('/cmdb/index/')
            return render(request,'index.html')
        # print(obj)
        
    # return render(request,'login.html')

def index(request):
    print("有请求")
    return render(request,'index.html')
    # return HttpResponse("hello word")

