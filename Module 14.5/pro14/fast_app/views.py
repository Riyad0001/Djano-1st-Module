from django.shortcuts import render
from . import forms
# Create your views here.

def homeView(request):
    data=forms.GetForm()
    return render(request,"home.html",{'form':data})

def modelView(request):
    std=forms.Pro()
    return render(request,"modeldata.html",{'st':std})

