from django import forms
from .models import Cemetery, Burial
from django.utils import timezone
from django.core.validators import MinLengthValidator
from .models import UserProfile
from django.contrib.auth.models import User


class CemeteryForm(forms.ModelForm):
    zipcode=forms.CharField(min_length=5, max_length=5)

    class Meta:
        model=Cemetery
        fields=('name','city','zipcode',)


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