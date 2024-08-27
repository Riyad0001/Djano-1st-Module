from django import forms
from django.forms import Textarea
from . import models
class AddfoodForm(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        super(forms.ModelForm,self).__init__(*args,**kwargs)
        # self.fields['food_catagory'].widget.attrs.update({'class':'form-control'})
        for fild in self.fields:
            self.fields[fild].widget.attrs.update({'class':'form-control'})
    
    class Meta:
        model = models.Food
        fields ="__all__"
        labels={
            'food_catagory':'Foods Catagory'
        }
        widgets={
            'food_description':Textarea(attrs={'rows':10})
        }