from django.shortcuts import render,redirect
from . import forms
from . import models
# Create your views here.

def add_catagory(request):
    if request.method=="POST":
        CatForm=forms.CatagoryForm(request.POST)
        if CatForm.is_valid:
            CatForm.save(commit=True)
            return redirect('add_catagory')
    else:
        CatForm=forms.CatagoryForm()


    return render(request,"add_catagory.html",{"form":CatForm})

def edit_cat(request,id):
    post=models.Catagory.objects.get(pk=id)
    CatForm=forms.CatagoryForm(instance=post)
    if request.method=="POST":
        CatForm=forms.CatagoryForm(request.POST,instance=post)
        if CatForm.is_valid:
            CatForm.save(commit=True)
            return redirect('view_cat')
    return render(request,"add_catagory.html",{"form":CatForm})

def delet_post(request,id):
    post=models.Catagory.objects.get(pk=id)
    post.delete()
    return redirect('view_cat')