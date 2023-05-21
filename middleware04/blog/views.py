from django.shortcuts import render,HttpResponse
from django.template.response import TemplateResponse
# Create your views here.

def home(request):
    print("I am Home View")
    return HttpResponse("This is Home4 page")


def excep(request):
    print("I am Exception View")
    a = 10 / 0
    return HttpResponse("This is Exception page")


def user_info(request):
    print("I am User Info View")
    context = { 'name' : 'Jiya'}
    return TemplateResponse(request, 'blog/user.html' ,context)