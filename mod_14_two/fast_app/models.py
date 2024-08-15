from django.db import models

# Create your models here.
class StudentModel(models.Model):
    roll=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=30)
    father_name=models.TextField()
    address=models.TextField(default="Tetulia")

    def __str__(self):
        return f"Name : {self.name}"
    