from django.db import models
from Brand.models import Brand
# Create your models here.
class Car(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    Brand=models.ForeignKey(Brand,on_delete=models.CASCADE)
    Image=models.ImageField(upload_to="Car/medias/uploads/",blank=True,null=True)

    def __str__(self):
        return self.name
    

class Comment(models.Model):
    car=models.ForeignKey(Car,on_delete=models.CASCADE,related_name="Comments")
    name=models.CharField(max_length=100)
    email=models.EmailField()
    body=models.TextField()
    created_on=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comments By {self.name}"
    


    


