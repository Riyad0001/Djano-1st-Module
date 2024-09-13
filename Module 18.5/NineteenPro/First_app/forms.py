from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# Create your models here.
 
class UserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['first_name','last_name','email','username']