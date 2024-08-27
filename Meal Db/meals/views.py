from django.shortcuts import render,redirect
from . import models
from . import forms
# Create your views here.
def show_meals(request):
    foods=models.Food.objects.all()
    return render(request,"meals\index.html",{'foods':foods})

def add_meals(request):
    if request.method=='POST':
        form=forms.AddfoodForm(request.POST,request.FILES)
        if form.is_valid():
            # print(form.cleaned_data)
            form.save()
            return redirect('homepage')


    form=forms.AddfoodForm()
    return render(request,"meals\meal.html",{'form':form})
