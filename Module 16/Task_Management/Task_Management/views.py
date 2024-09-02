from django.shortcuts import render
from task import models

def home(request):
    data=models.TaskModel.objects.prefetch_related('catagory_name').all()
    return render(request,"home.html",{'data':data})