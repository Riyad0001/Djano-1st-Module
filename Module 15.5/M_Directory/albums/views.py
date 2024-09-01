from django.shortcuts import render,redirect
from . import forms
from . import models
# Create your views here.
def home(request):
    if request.method=="POST":
        form=forms.add_albums(request.POST)
        if form.is_valid:
            form.save()
            return redirect('homepage')
    else:
        form=forms.add_albums()
    return render(request,'albm.html',{'form':form})
def edit_albm(request,id):
    post=models.Album.objects.get(pk=id)
    form=forms.add_albums(instance=post)
    if request.method=="POST":
        form=forms.add_albums(request.POST,instance=post)
        if form.is_valid:
            form.save()
            return redirect('homepage')
    return render(request,'albm.html',{'form':form})

def delet_albm(request,id):
    post=models.Album.objects.get(pk=id)
    post.delete()
    return redirect('homepage')