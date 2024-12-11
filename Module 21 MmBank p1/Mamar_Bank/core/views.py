from django.shortcuts import render,redirect
from django.views.generic import TemplateView
# Create your views here.

class HomeVaw(TemplateView):
    template_name='index.html'
