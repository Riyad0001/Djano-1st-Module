from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=20)
    roll=models.IntegerField(primary_key=True)
    addres=models.TextField()
    section=models.TextField(default="rIYADS")

    def __str__(self):
        return f"{self.name}, Roll: {self.roll}" 
    