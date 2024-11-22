from django.shortcuts import render
from . import forms
# Create your views here.

def registerForm(request):
    if request.method=="POST":
        reg_form=forms.Registratin_form(request.POST)
        if reg_form.is_valid:
            reg_form.save(commit=True)
            messages.success(request,"Registered Successsfully!")
            return redirect('homepage')
    else:
        reg_form=forms.Registratin_form()
    return render(request,'register.html',{'form':reg_form})