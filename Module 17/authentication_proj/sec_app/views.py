from django.shortcuts import render,redirect
from . import forms
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
# Create your views here.
def home(request):
    return render(request,'home.html')
def signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = forms.RegisterForm(request.POST)
            try:
                if form.is_valid():
                    form.save()
                    messages.success(request, "Account Created Successfully")
                    print(form.cleaned_data)
            except ValueError as e:
                # Handle ValueError and provide feedback to the user
                messages.error(request, f"An error occurred: {str(e)}. Please correct the data and try again.")
        else:
            form = forms.RegisterForm()

        return render(request, './signup.html', {'form': form})
    else:
        return redirect('profile')


def login_page(request):
    if not request.user.is_authenticated:
        if request.method=="POST":
            form=AuthenticationForm(request=request,data=request.POST)
            if form.is_valid():
                name=form.cleaned_data['username']
                passward=form.cleaned_data['password']
                user=authenticate(username=name,password=passward)
                if user is not None:
                    login(request,user)
                    return redirect('profile')
        else:
            form=AuthenticationForm()
        return render(request, './login.html', {'form': form})
    else:
        return redirect('profile')

def profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = forms.change_data(request.POST,instance=request.user)
            if form.is_valid():
                messages.success(request, "Account Updated Successfully")
                form.save()
        else:
            form = forms.change_data(instance=request.user)

        return render(request, './profile.html', {'form': form})
    else:
        return redirect('signup')

def loged_out(request):
    logout(request)
    return redirect('login')

def change_pass(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            form=PasswordChangeForm(user=request.user,data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request,request.user)
                return redirect('profile')
        else:
            form=PasswordChangeForm(user=request.user)
        return render(request,"pass_cng.html",{'form':form})
    else:
        return redirect('login')
def change_pass2(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            form=SetPasswordForm(user=request.user,data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request,request.user)
                return redirect('profile')
        else:
            form=SetPasswordForm(user=request.user)
        return render(request,"pass_cng.html",{'form':form})
    else:
        return redirect('login')

def change_dat(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = forms.change_data(request.POST,isinstance=request.user)
            if form.is_valid():
                form.save()
                messages.success(request, "Account Updated Successfully")
        else:
            form = forms.change_data()

        return render(request, './profile.html', {'form': form})
    else:
        return redirect('signup')