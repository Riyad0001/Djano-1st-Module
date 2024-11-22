from django import forms
from .models import UserCreationmodel,AddressModel,User
from .constants import ACCOUNT_TYPE,GENDER
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
class AccountForm(UserCreationForm):
    birthdate=forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    account_type=forms.ChoiceField(choices=ACCOUNT_TYPE)
    gender=forms.ChoiceField(choices=GENDER)
    postal_code=forms.IntegerField()
    country=forms.CharField(max_length=100)
    street_address=forms.CharField(max_length=100)
    city=forms.CharField(max_length=100)


    class Meta:
        model=User
        fields=['username','email','first_name','last_name','password1','password2','birthdate','account_type','gender','postal_code','country','street_address','city']

    def save(self,commit=True):
        our_user=super().save(commit=False)
        print("Creating User:", our_user)
        if commit:
            our_user.save()
            print("User Saved:", our_user.id)
            account_type=self.cleaned_data.get('account_type')
            gender=self.cleaned_data.get('gender')
            postal_code=self.cleaned_data.get('postal_code')
            country=self.cleaned_data.get('country')
            birthdate=self.cleaned_data.get('birthdate')
            city=self.cleaned_data.get('city')
            street_address=self.cleaned_data.get('street_address')

            AddressModel.objects.create(
                user=our_user,
                postal_code=postal_code,
                country=country,
                city=city,
                street_address=street_address

            )
            UserCreationmodel.objects.create(
                user=our_user,
                account_type=account_type,
                gender=gender,
                birthdate=birthdate,
                account_no=1000+our_user.id

            )
        return our_user
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        common_classes = (
        "appearance-none block w-full bg-gray-200 "
        "text-gray-700 border border-gray-200 rounded "
        "py-3 px-4 leading-tight focus:outline-none "
        "focus:bg-white focus:border-gray-500"
        )
        for field in self.fields.values():
            field.widget.attrs.update({'class': common_classes})

class UserupdtForm(forms.ModelForm):
    birthdate=forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    account_type=forms.ChoiceField(choices=ACCOUNT_TYPE)
    gender=forms.ChoiceField(choices=GENDER)
    postal_code=forms.IntegerField()
    country=forms.CharField(max_length=100)
    street_address=forms.CharField(max_length=100)
    city=forms.CharField(max_length=100)

    class Meta:
        model=User
        fields=['first_name','last_name','email']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        common_classes = (
        "appearance-none block w-full bg-gray-200 "
        "text-gray-700 border border-gray-200 rounded "
        "py-3 px-4 leading-tight focus:outline-none "
        "focus:bg-white focus:border-gray-500"
        )
        for field in self.fields.values():
            field.widget.attrs.update({'class': common_classes})

        if self.instance:
            try:
                user_account=self.instance.account
                user_address=self.instance.address
            except UserCreationmodel.DoesNotExist:
                user_account=None
                user_address=None
            
            if user_account:
                self.fields['account_type'].initial = user_account.account_type
                self.fields['gender'].initial = user_account.gender
                self.fields['birthdate'].initial = user_account.birthdate
                self.fields['street_address'].initial = user_address.street_address
                self.fields['city'].initial = user_address.city
                self.fields['postal_code'].initial = user_address.postal_code
                self.fields['country'].initial = user_address.country

    def save(self,commit=True):
        our_user=super().save(commit=False)
        if commit:
            our_user.save()
            user_account,created=UserCreationmodel.objects.get_or_create(user=user)
            user_address,created=AddressModel.objects.get_or_create(user=user)
            user_account.account_type=self.cleaned_data['account_type']
            user_account.gender=self.cleaned_data['gender']
            user_account.birthdate=self.cleaned_data['birthdate']
            user_account.save()

            user_address.postal_code=self.cleaned_data['postal_code']
            user_address.country=self.cleaned_data['country']
            user_address.city=self.cleaned_data['city']
            user_address.street_address=self.cleaned_data['street_address']
            
        return our_user





