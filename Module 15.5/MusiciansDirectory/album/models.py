from django.db import models
from musician.models import Musician
# Create your models here.

class Album(models.Model):
    Album_name=models.CharField(max_length=40)
    Musician_name=models.ForeignKey(Musician,on_delete=models.CASCADE)
    Relase_date=models.DateField()
    Rating=models.Mul
