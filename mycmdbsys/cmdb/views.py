from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.

def login(request):
    if request.method=="GET":
        return render(request,'login.html')
    elif request.method=="POST":
        # 获取前台提交过来的用户名与密码
        u=request.POST.get('user')
        p=request.POST.get('pwd')
        
    return render(request,'login.html')

def index(request):
    return render(request,'index.html')
    return HttpResponse("hello word")