from django.shortcuts import render,redirect
from . import forms
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from post import models as post_model
from django.contrib.auth.views import LoginView,LogoutView
from django.urls import reverse_lazy
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
            messages.success(request,"Registered Successsfully!")
            return redirect('homepage')
    else:
        reg_form=forms.Registratin_form()
    return render(request,'register.html',{'form':reg_form,'type':'Register'})

def LoginForm(request):
    if request.method=='POST':
        log_form=AuthenticationForm(request,request.POST)
        if log_form.is_valid():
            username=log_form.cleaned_data['username']
            userpass=log_form.cleaned_data['password']
            user=authenticate(username=username,password=userpass)
            if user is not None:
                login(request,user)
                messages.success(request,"LogedIn Successsfully!")
                return redirect('profile')
            else:
                messages.warning(request,"Wrong Information")
                return redirect('register')
    else:
        log_form=AuthenticationForm()
    return render(request,'register.html',{'form':log_form,'type':'LogINN'})
def logedOut(request):
    logout(request)
    return redirect('login')

@login_required()       
def ProfileEdt(request):
    if request.method=="POST":
        p_form=forms.ProfileUpdt(request.POST,instance=request.user)
        if p_form.is_valid:
            p_form.save(commit=True)
            messages.success(request,"Profile Updated Successsfully!")
            return redirect('edt_profile')
    else:
        p_form=forms.ProfileUpdt(instance=request.user)
    return render(request,'edit_profile.html',{'form':p_form})
@login_required()       
def Cng_Pass(request):
    if request.method=="POST":
        form=PasswordChangeForm(request.user,data=request.POST)
        if form.is_valid():
            form.save(commit=True)
            messages.success(request,"Password Updated Successsfully!")
            update_session_auth_hash(request,form.user)
            return redirect('edt_profile')
    else:
        form=PasswordChangeForm(user=request.user)
    return render(request,'cng_pass.html',{'form':form})

@login_required()       
def Profile(request):
    ata=post_model.Post.objects.filter(author=request.user)
    return render(request,'profile.html',{'data':ata})

class UserLoginView(LoginView):
    template_name="register.html"
    # success_url=reverse_lazy('profile')
    def get_success_url(self):
        return reverse_lazy('profile')
    def form_valid(self,form):
        messages.success(self.request,"Loged In Successfuly")
        return super().form_valid(form)
        
    def form_invalid(self,form):
        messages.success(self.request,"Loged In Information wrong")
        return super().form_invalid(form)
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['type']='LogIn'
        return context
