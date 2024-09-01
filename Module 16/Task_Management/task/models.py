from django.db import models
from catagory.models import CatModel
# Create your models here.
class TaskModel(models.Model):
    taskTitle =models.CharField(max_length=100)
    taskDescription=models.TextField()
    is_completed=models.BooleanField(default=False)
    Assign_Date=models.DateField()
    catagory_name=models.ManyToManyField(CatModel)


    def __str__(self):
        return self.taskTitle
    