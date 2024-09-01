from django.shortcuts import render,redirect
from . import forms
# Create your views here.
def add_cat(request):
    if request.method=="POST":
        form=forms.CatForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('homepage')
    else:
        form=forms.CatForm()

    return render(request,"add_cat.html",{'form':form})