from django import forms
from .models import Cemetery, Burial
from django.utils import timezone
from django.core.validators import MinLengthValidator


class CemeteryForm(forms.ModelForm):
    class Meta:
        model=Cemetery
        fields=('name','city','zipcode',)

        validators={
            'zipcode':MinLengthValidator(5),
            }


class BurialForm(forms.ModelForm):
    class Meta:
        model=Burial
        fields=('cemetery_id','first_name','DoB','DoD','sex',)

        widgets = {
            'DoB' : forms.TextInput(attrs = {'placeholder': 'YYYY-MM-DD','class':'datepicker'}),
            'DoD' : forms.TextInput(attrs = {'placeholder': 'YYYY-MM-DD','class':'datepicker'}),
        }

