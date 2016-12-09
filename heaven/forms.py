from django import forms
from .models import Cemetery, Burial
from django.utils import timezone
from django.core.validators import MinLengthValidator


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

