from django.shortcuts import render
from post import models as post_model
from catagory import models as cat_model
def home(request):
    data=post_model.Post.objects.all()
    return render(request,"home.html",{'data':data})
def view_cat(request):
    data=cat_model.Catagory.objects.all()
    return render(request,"aut.html",{'data':data})