from django.shortcuts import render
from django.urls import reverse_lazy
# Create your views here.
from . import forms
from . import models
from django.views.generic.edit import FormView
from django.views.generic import CreateView,UpdateView,DeleteView,DetailView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.messages.views import SuccessMessageMixin
@method_decorator(login_required, name='dispatch')
class AddMusiView(CreateView,SuccessMessageMixin):
    template_name="Add_musi.html"
    form_class=forms.MusicianForm
    success_url=reverse_lazy("homepage")
    model=models.Musi
    success_message="Musician Added Sucessfully"
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
@method_decorator(login_required, name='dispatch')
class EditMusi(UpdateView,SuccessMessageMixin):
    template_name="Add_musi.html"
    success_url=reverse_lazy("homepage")
    model=models.Musi
    form_class=forms.MusicianForm
    pk_url_kwarg="id"
    success_message="Musician Added Sucessfully"
class SignupView(CreateView,SuccessMessageMixin):
    template_name="signup.html"
    success_url=reverse_lazy("login")
    form_class=forms.SignupForm
    success_message="Account Created Sucessfully"
    

