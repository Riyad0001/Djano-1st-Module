from django.shortcuts import render
from django.views.generic import FormView
from django.contrib.auth import login,logout
from .forms import AccountForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView,LogoutView
# Create your views here.

class RegFormView(FormView):
    template_name='accounts/signup.html'
    success_url=reverse_lazy('home')
    form_class=AccountForm
    
    def form_valid(self, form):
        print("Cleaned Data:", form.cleaned_data)
        user=form.save()
        if not user:
            raise ValueError("User creation failed!")
        login(self.request,user)
        return super().form_valid(form)

class LoginVieww(LoginView):
    template_name='accounts/login.html'
    def get_success_url(self):
        return reverse_lazy('home')

class LgOutview(LogoutView):
    def get_success_url(self):
        if self.request.user.is_authenticated:
            logout(self.request)
        return reverse_lazy('home')

