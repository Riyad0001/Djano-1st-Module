from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from .constants import ACCOUNT_TYPE,GENDER
class UserCreationmodel(models.Model):
    user=models.OneToOneField(User,related_name="user",on_delete=models.CASCADE)
    account_type=models.CharField(max_length=15,choices=ACCOUNT_TYPE)
    account_no=models.IntegerField(unique=True)
    birthdate=models.DateField()
    gender=models.CharField(max_length=10,choices=GENDER)
    balance=models.DecimalField(default=0,decimal_places=2,max_digits=13)
    initial_deposite_date=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.first_name
    


class AddressModel(models.Model):
    user=models.OneToOneField(User,related_name="adress",on_delete=models.CASCADE)
    postal_code=models.IntegerField()
    country=models.CharField(max_length=100)
    street_address=models.CharField(max_length=100)
    city=models.CharField(max_length=100)

    def __str__(self):
        return self.user.email
    


