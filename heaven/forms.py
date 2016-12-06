from django import forms
from .models import Cemetery, Burial
from django.utils import timezone

class CemeteryForm(forms.ModelForm):
    class Meta:
        model=Cemetery
        fields=('name','city','zipcode',)

class BurialForm(forms.ModelForm):
    class Meta:
        model=Burial
        fields=('cemetery_id','first_name','DoB','DoD','sex',)

