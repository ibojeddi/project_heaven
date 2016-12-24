from decimal import Decimal
from django import forms
from .models import Cemetery, Burial
from django.utils import timezone
from django.core.validators import MinLengthValidator
from .models import UserProfile
from django.contrib.auth.models import User


class CemeteryForm(forms.ModelForm):
    zipcode=forms.CharField(min_length=5, max_length=5,
                            widget=forms.NumberInput(attrs={'placeholder': '5 Digits'}))
    latitude=forms.DecimalField(max_digits=8, decimal_places=6,min_value=-85.05115,max_value=85.05115,
                                widget=forms.NumberInput(attrs={'placeholder': '0.000,000  ( -85 to 85 )','style':'width:200px'}))
    longitude=forms.DecimalField(max_digits=9, decimal_places=6,min_value=-180,max_value=180,
                                 widget=forms.NumberInput(attrs={'placeholder': '0.000,000  ( -180 to 180 )','style':'width:200px'}))

    class Meta:
        model=Cemetery
        fields=('name','city','zipcode','latitude','longitude')

class BurialForm(forms.ModelForm):
    class Meta:
        model=Burial
        fields=('cemetery_id','first_name','DoB','DoD','sex',)

        widgets = {
            'DoB' : forms.TextInput(attrs = {'placeholder': 'YYYY-MM-DD','class':'datepicker'}),
            'DoD' : forms.TextInput(attrs = {'placeholder': 'YYYY-MM-DD','class':'datepicker'}),
        }

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture')