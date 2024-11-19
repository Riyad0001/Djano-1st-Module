from django.db import models
from Brand.models import Brand
# Create your models here.
from django.contrib.auth.models import User
class Car(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    Brand=models.ForeignKey(Brand,on_delete=models.CASCADE)
    Quantity=models.IntegerField(null=True,blank=True)
    Description=models.TextField(blank=True,null=True)
    Image=models.ImageField(upload_to="Car/medias/uploads/",blank=True,null=True)

    def __str__(self):
        return self.name
    

class Comment(models.Model):
    car=models.ForeignKey(Car,on_delete=models.CASCADE,related_name="comments")
    name=models.CharField(max_length=100)
    email=models.EmailField()
    body=models.TextField()
    created_on=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comments By {self.name}"

class Buyed(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="purchases")
    car=models.ForeignKey(Car,on_delete=models.CASCADE,related_name="purchases")
    date=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user
    
    


    


