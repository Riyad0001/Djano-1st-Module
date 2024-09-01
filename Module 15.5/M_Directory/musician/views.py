from django.shortcuts import render,redirect
from . import forms
from . import models
# Create your views here.
def add_Musi(request):
    if request.method=="POST":
        form=forms.add_musician(request.POST)
        if form.is_valid:
            form.save()
            return redirect('homepage')
    else:
        form=forms.add_musician()
    return render(request,'add_musi.html',{'form':form})

def edit_musi(request,id):
    post=models.Musician.objects.get(pk=id)
    form=forms.add_musician(instance=post)
    if request.method=="POST":
        form=forms.add_musician(request.POST,instance=post)
        if form.is_valid:
            form.save()
            return redirect('homepage')
    return render(request,'add_musi.html',{'form':form})