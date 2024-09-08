from django.shortcuts import render,redirect
from . import forms
from . import models
# Create your views here.

def add_post(request):
    if request.method=="POST":
        PoForm=forms.PostForm(request.POST)
        if PoForm.is_valid:
            PoForm.save(commit=True)
            return redirect('add_post')
    else:
        PoForm=forms.PostForm()
    return render(request,"add_post.html",{"form":PoForm})

def edit_post(request,id):
    post=models.Post.objects.get(pk=id)
    PoForm=forms.PostForm(instance=post)
    if request.method=="POST":
        PoForm=forms.PostForm(request.POST,instance=post)
        if PoForm.is_valid:
            PoForm.save(commit=True)
            return redirect('homepage')
    return render(request,"add_post.html",{"form":PoForm})

def delet_post(request,id):
    post=models.Post.objects.get(pk=id)
    post.delete()
    return redirect('homepage')