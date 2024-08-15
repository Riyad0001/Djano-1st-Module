from .models import Catagory
from django import forms
class CatagoryForm(forms.ModelForm):
    
    class Meta:
        model = Catagory
        fields = "__all__"
