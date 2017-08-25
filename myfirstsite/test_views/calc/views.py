from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

def old_add2_redirect(request,a,b):
    return HttpResponseRedirect(reverse('add2',args=(a,b)))

def index(request):
    return render(request,'home.html')

def add(request):
    a=request.GET['a']
    b=request.GET['b']
    # c=(int)a+(int)b
    # c=(int)a +(int)b
    c=int(a) + int(b)
    return HttpResponse(str(c))

def add2(request,a,b):
    c=int(a)+int(b)
    return HttpResponse(str(c))
# Create your views here.

# urlpatterns=patterns('',url(r'^add/(\d+)/(\d+)/$','app.views.add',name='add'))
#
# {%url 'add' 4 5%}