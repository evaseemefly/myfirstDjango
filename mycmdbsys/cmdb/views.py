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
            # return render(request,'index.html')
        # print(obj)
        
    # return render(request,'login.html')

def index(request):
    print("有请求")
    return render(request,'index.html')
    # return HttpResponse("hello word")

def user_info(request):
    # 获取全部联系人集合
    user_list=models.UserInfo.objects.all()

    # render函数的第三个参数，是字典形式的模板参数
    return render(request,'user_info.html',{'user_list':user_list})

def userdetail(request,uid):
    # 从数据库根据uid返回指定用户的信息
    obj=models.UserInfo.objects.filter(id=uid).first()

    return render(request,'user_detail.html',{'obj':obj})

def userdel(request,uid):
    obj=models.UserInfo.objects.filter(id=uid).delete()
    return redirect('/cmdb/user_info/')
