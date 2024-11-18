from django.shortcuts import render
from Brand import models
from Car import models
def home(request,brand_slug=None):
    data=models.Car.objects.all()
    if brand_slug is not None:
        brand=models.Brand.objects.get(slug=brand_slug)
        data=models.Car.objects.filter(Brand=brand)
    brand=models.Brand.objects.all()
    return render(request,'home.html',{'data':data,'brand':brand})
