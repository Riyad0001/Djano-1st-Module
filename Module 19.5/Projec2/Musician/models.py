from django.db import models

# Create your models here.

class Musi(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    email=models.EmailField()
    number=models.CharField(max_length=15)
    Instrument_type=models.CharField(max_length=100)

    def __str__(self):
        return self.first_name

    
