from django.shortcuts import render,redirect
from . import forms
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