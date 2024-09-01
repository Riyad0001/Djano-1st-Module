from django.db import models
# Create your models here.
class Musician(models.Model):
    Fsat_name=models.CharField(max_length=60)
    Last_name=models.CharField(max_length=60)
    Email=models.EmailField()
    Phone=models.IntegerField(max_length=30)
    Instrument_type=models.CharField(max_length=30)

    def __str__(self):
        return self.Fsat_name
    