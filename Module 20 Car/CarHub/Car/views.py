from django.shortcuts import render
from . import forms
from django.views.generic.edit import CreateView
# Create your views here.
from django.urls import reverse_lazy

class SignUpForm(CreateView):
    form_class=forms.RegisterForm
    template_name="signup.html"
    success_url=reverse_lazy('home')
    