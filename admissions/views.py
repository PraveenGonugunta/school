from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request,'index.html',{})

def love(request):
    return render(request,'love.html',{})

def hate(request):
    return render(request,'hate.html',{})

def login(request):
    return render(request,'login.html',{})
