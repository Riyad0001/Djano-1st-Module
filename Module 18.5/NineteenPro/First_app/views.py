from django.shortcuts import render,redirect
from . import forms
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm,SetPasswordForm,AuthenticationForm
from django.contrib.auth import update_session_auth_hash,login,logout,authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.


def signup(request):
    if request.method=="POST":
        form=forms.UserForm(request.POST)
        if form.is_valid():
            messages.success(request,"REgistered Successfully")
            form.save(commit=True)
            return redirect('homepage')
    else:
        form=forms.UserForm(request.POST)
    return render(request,'signup.html',{'form':form,'type':'Sign Up'})
@login_required
def profile(request):
    return render(request,'profile.html')

@login_required
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
@login_required
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
        form=AuthenticationForm(request,request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                messages.success(request,"Loged In Succesfuly")
                return redirect('homepage')
            else:
                messages.warning(request,"wrong Information")
                return redirect('register')
    else:
        form=AuthenticationForm()
    return render(request,'signup.html',{'form':form,'type':'LogIn'})
@login_required
def logout_user(request):
    logout(request)
    return redirect('login')