from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def welcome(request):
    return HttpResponse("<h1>欢迎来到我的django</h1>")