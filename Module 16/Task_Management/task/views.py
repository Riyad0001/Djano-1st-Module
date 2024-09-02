from django.shortcuts import render,redirect
from . import forms
from . import models
# Create your views here.
def add_task(request):
    if request.method=="POST":
        form=forms.TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form=forms.TaskForm()
    return render(request,"add_task.html",{'form':form})
def edit_task(request,id):
    post=models.TaskModel.objects.get(pk=id)
    form=forms.TaskForm(instance=post)
    if request.method=="POST":
        form=forms.TaskForm(request.POST,instance=post)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    return render(request,"add_task.html",{'form':form})

def delete_task(request,id):
    post=models.TaskModel.objects.get(pk=id)
    post.delete()
    return redirect('homepage')