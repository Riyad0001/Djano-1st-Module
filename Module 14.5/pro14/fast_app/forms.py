from django import forms
from django.forms.widgets import NumberInput
from fast_app.models import Product


BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']
FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
]

class GetForm(forms.Form):
    name=forms.CharField(widget=forms.Textarea)
    tk=forms.IntegerField()
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows':3}),initial="Good")
    email=forms.EmailField()
    agree=forms.BooleanField()
    date=forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    message = forms.CharField(max_length = 10,)
    email_address = forms.EmailField(label="Please enter your email address")
    favorite_color = forms.ChoiceField(choices=FAVORITE_COLORS_CHOICES)
    favorite_color_2 = forms.ChoiceField(widget=forms.RadioSelect, choices=FAVORITE_COLORS_CHOICES)
    favorite_colors = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=FAVORITE_COLORS_CHOICES,)

class Pro(forms.ModelForm):
    class Meta:
        model=Product
        fields="__all__"


    



