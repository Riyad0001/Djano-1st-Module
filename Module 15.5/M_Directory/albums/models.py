from django.db import models
from musician.models import Musician
# Create your models here.
MY_CHOICES = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )
class Album(models.Model):
    Album_name=models.CharField(max_length=40)
    Musician_name=models.ForeignKey(Musician,on_delete=models.CASCADE)
    Relase_date=models.DateField()
    Rating=models.CharField(max_length=1,choices=MY_CHOICES)

    def __str__(self):
        return self.Album_name
    