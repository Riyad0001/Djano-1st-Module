from django.db import models

# Create your models here.

class Brand(models.Model):
    name=models.CharField(max_length=40)
    slug=models.SlugField(max_length=100,null=True,unique=True,blank=True)

    def __str__(self):
        return self.name
    
