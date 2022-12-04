from django.shortcuts import render
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
        pass

class SuccessView(View):
    def get(self,request):
        return render(request,'home/success.html')

