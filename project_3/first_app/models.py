from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=20)
    roll=models.IntegerField(primary_key=True)
    section=models.TextField()
    addres=models.TextField(default="Ryaan")