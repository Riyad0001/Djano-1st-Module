from django.db import models

# Create your models here.

class Catagory(models.Model):
    catagory_name=models.CharField(max_length=50)

    def __str__(self):
        return self.catagory_name
    

class Food(models.Model):
    food_name=models.CharField(max_length=100)
    food_description=models.TextField()
    food_catagory=models.ForeignKey(Catagory,on_delete=models.CASCADE)
    food_image=models.ImageField(upload_to="meals/images",default="media/meals/default.jpg")

    def __str__(self):
        return self.food_name
    
    
