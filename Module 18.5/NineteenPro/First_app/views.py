from django.shortcuts import render,redirect
from . import forms
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm,SetPasswordForm
from django.contrib.auth import update_session_auth_hash,login,logout
# Create your views here.


def signup(request):
    if request.method=="POST":
        form=forms.UserForm(request.POST)
        if form.is_valid():
            messages.success(request,"REgistered Successfully")
            form.save(commit=True)
            return redirect('profile')
    else:
        form=forms.UserForm(request.POST)
    return render(request,'signup.html',{'form':form})
def profile(request):
    return render(request,'profile.html')


def change_pass(request):
    if request.method=="POST":
        form=PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,user)
            messages.success(request,"Password Update Succesfuly")
            return redirect('profile')
    else:
        form=PasswordChangeForm(request.user)
    return render(request,'cng_pass.html',{'form':form})
def change_pass2(request):
    if request.method=="POST":
        form=SetPasswordForm(request.user,request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,request.user)
            messages.success(request,"Password Update Succesfuly")
            return redirect('profile')
    else:
        form=SetPasswordForm(request.user)
    return render(request,'cng_pass.html',{'form':form})

def login_user(request):
    if request.method=="POST":
        username=