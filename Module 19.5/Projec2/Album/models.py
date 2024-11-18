from django.db import models
from Musician.models import Musi
# Create your models here.

class Album(models.Model):
    A_name=models.CharField(max_length=100)
    Musician=models.ForeignKey(Musi,on_delete=models.CASCADE)
    release_date=models.DateField()
    rating = models.PositiveIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])

    def __str__(self):
        return self.A_name

    