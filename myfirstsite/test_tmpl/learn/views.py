from django.shortcuts import render

# Create your views here.
# def home(request):
#     return render(request,'home.html')

# 返回string类型的字符串
# def home(request):
#     string =u"django"
#     return render(request,'home.html',{'string':string})

def home(request):
    TutorialList=["Html","css","jquery","python"]
    return render(request,'home.html',{'TutorialList':TutorialList})

# 返回字典
# def home(request):
#     info_dict={'site':u'drno','content':u'内容测试内容测试'}
#     return render(request,'home.html',{'info_dic':info_dict})

def home(request):
    List=map(str,range(100))
    return render(request,'home.html',{'List':List})




