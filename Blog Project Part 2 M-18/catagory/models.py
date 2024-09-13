from django.db import models

# Create your models here.
class Catagory(models.Model):
    name=models.CharField(max_length=100)
    slug=models.SlugField(max_length=100,blank=True,null=True,unique=True)
    def __str__(self):
        return self.name


    