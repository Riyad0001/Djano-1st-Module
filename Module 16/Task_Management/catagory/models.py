from django.db import models

# Create your models here.
class CatModel(models.Model):
    catagory_name=models.CharField(max_length=50)
    

    def __str__(self):
        return self.catagory_name
    