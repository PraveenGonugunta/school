from django.shortcuts import render
from django.http import HttpResponse
from admissions.models import Admission
from admissions.forms import admission

# Create your views here.

def home(request):
    data=Admission.objects.all()
    form_data=admission()
    res= render(request,'index.html',{'data':data,'form_data':form_data})
    return res

def love(request):
    return render(request,'love.html',{})

def hate(request):
    return render(request,'hate.html',{})

def login(request):
    return render(request,'login.html',{})
