from django.shortcuts import render
from django.http import HttpResponse
from admissions.models import Admission

# Create your views here.

def home(request):
    data=Admission.objects.all()
    res= render(request,'index.html',{'data':data})
    return res

def love(request):
    return render(request,'love.html',{})

def hate(request):
    return render(request,'hate.html',{})

def login(request):
    return render(request,'login.html',{})
