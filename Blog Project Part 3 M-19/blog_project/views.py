from django.shortcuts import render
from post import models as post_model
from catagory.models import Catagory
def home(request,catagory_slug=None):
    data=post_model.Post.objects.all()
    if catagory_slug is not None:
        catagory=Catagory.objects.get(slug=catagory_slug)
        data=post_model.Post.objects.filter(catagory=catagory)
    catagory=Catagory.objects.all()
    return render(request,"home.html",{'data':data,'catagory':catagory})
def view_cat(request):
    data=Catagory.objects.all()
    return render(request,"aut.html",{'data':data})