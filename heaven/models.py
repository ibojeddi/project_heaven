from django.db import models
from django.utils import timezone


class Cemetery(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(verbose_name="Cemetery Name",max_length=100)
    city=models.CharField(max_length=30)
    zipcode=models.CharField(max_length=5)
    date_created=models.DateTimeField(editable=False, auto_now_add=True)
    date_modified= models.DateTimeField(editable=False, auto_now=True)
    created_by=models.ForeignKey('auth.User')

    def __str__(self):
        return  str(self.id) +'-' + self.name + ' -  ' + self.city

class Burial(models.Model):
    id = models.AutoField(primary_key=True)
    cemetery_id=models.ForeignKey( Cemetery,on_delete=models.CASCADE, verbose_name="Cemetery ID")
    first_name=models.CharField(max_length=30, verbose_name="First Name")
    DoB=models.DateField(blank=True, null=True, verbose_name="Date of Birth")
    DoD=models.DateField(blank=True, null=True,verbose_name="Date of Death")

    '''Sex Options'''
    MALE='M'
    FEMALE='F'
    UNKNOWN='U'
    sex_choices=((MALE,'Male'),(FEMALE,'Female'),(UNKNOWN,'Unknown'))
    sex=models.CharField(max_length=1,choices=sex_choices)

    date_created=models.DateTimeField(editable=False, auto_now_add=True)
    created_by=models.ForeignKey('auth.User')

    def __str__(self):
        return self.first_name