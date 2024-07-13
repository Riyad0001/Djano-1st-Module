from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def courses(request):
    return HttpResponse("This is Course Page")
def about(request):
    return HttpResponse("This is Aboutttttttttt Page")
def fukka(request):
    return HttpResponse("This is fukka Page")
