from django.shortcuts import render,redirect
from . import models
# Create your views here.
def home(request):
    # data=models.Student.objects.all()
    data = models.Student.objects.filter(roll__gte=0)
    return render(request,'home.html',{'data':data})

def delet_student(request,roll):
    std=models.Student.objects.get(pk=roll).delete()
    return redirect("/")
    