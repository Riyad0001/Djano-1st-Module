from django import forms
from fast_app.models import StudentModel

class StudentForm(forms.ModelForm):
    class Meta:
        model=StudentModel
        fields='__all__'
        # exclude=['name','roll']
        labels={'name':'Student Name','roll':'Stu Roll','address':"Student Home"}
        widgets={
            'name':forms.TextInput(attrs={'class': 'box-shadow'}),
            'roll':forms.PasswordInput()
        }
        help_texts={
            'name':"Write Your Full Name"
        }
        error_messages={
            'name':{
                'required':"fytfytfyty"
            }
        }