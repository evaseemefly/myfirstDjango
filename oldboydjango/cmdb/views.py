from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect

USER_LIST=[
    {'username': 'alex', 'email': 'asdfasdf', "gender": '男'},
    {'username': 'eriuc', 'email': 'asdfasdf', "gender": '男'},
    {'username': 'seven', 'email': 'asdfasdf', "gender": '男'},
]

def home(request):
    # return render(request, 'home.html')
    if request.method=="POST":
        # pass
        user=request.POST.get('username')
        email=request.POST.get('email')
        gender=request.POST.get('gender')
        temp={'username':user,'email':email,'gender':gender}
        USER_LIST.append(temp)
    # return HttpResponse('<h1>CMDB</h1>')
    # return render(request, '/home', {'user_list': USER_LIST})
    return render(request,'home.html',{'user_list':USER_LIST})

def login(request):
    # return (request,'login.html')
    error_msg=""
    # 若请求为POST请求，则回去提交过来的响应的数据
    if request.method=="POST":
        user=request.POST.get('user',None)
        pwd=request.POST.get('pwd',None)
        if user=='root' and pwd=='123':
            # 使用redirect时需要添加引用
            return redirect('/home')
            # return render(request,'/home')
        else:
            error_msg='用户名或密码错误'
    return render(request,'login.html',{'error_msg':error_msg})
    # return render(request,'login.html')