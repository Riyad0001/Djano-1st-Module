from django.shortcuts import render,redirect
from . import forms
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.
# def add_author(request):
#     if request.method=="POST":
#         author_form=forms.AuthorForm(request.POST)
#         if author_form.is_valid:
#             author_form.save(commit=True)
#             return redirect('add_author')
#     else:
#         author_form=forms.AuthorForm()
#     return render(request,'add_author.html',{'form':author_form})
def registerForm(request):
    if request.method=="POST":
        reg_form=forms.Registratin_form(request.POST)
        if reg_form.is_valid:
            reg_form.save(commit=True)
            return redirect('register')
    else:
        reg_form=forms.Registratin_form()
    return render(request,'register.html',{'form':reg_form})

def LoginForm(request):
    if request.method=='POST':
        log_form=AuthenticationForm(request.POST)
        if log_form.is_valid():
            username=log_form.cleaned_data['username']
            userpass=log_form.cleaned_data['password']
            