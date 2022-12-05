from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from . import models

# Create your views here.
# def home(request):
#     return render(request,'home/index.html')

# Class Based Views
class HomeView(View):
    def get(self,request):
        return render(request,'home/index.html')
    
class Registration(View):
    def get(self,request):
        return render(request,'home/register.html')
    def post(self,request):
        name = request.POST['name']
        dob = request.POST['dob']
        email = request.POST['email']
        passwd = request.POST['password']
        db = models.Table(name=name,dob=dob,email=email,password=passwd)
        db.save()
        return redirect('success')

class SuccessView(View):
    def get(self,request):
        return render(request,'home/success.html')

class StatusView(View):
    def get(self,request):
        data = models.Table.objects.all()
        return render(request,'home/status.html',context={'data':data})

class LoginView(View):
    def get(self,request):
        return render(request,"home/login.html")
        