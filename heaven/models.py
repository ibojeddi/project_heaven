from decimal import Decimal
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Cemetery(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(verbose_name="Cemetery Name",max_length=100)
    city=models.CharField(max_length=30)
    zipcode=models.CharField(max_length=5)
    latitude=models.DecimalField(default=Decimal('0.000000'),max_digits=8, decimal_places=6,
                                 validators=[MinValueValidator(-85.05115), MaxValueValidator(85.05115)])
    longitude=models.DecimalField(default=Decimal('0.000000'),max_digits=9, decimal_places=6,
                                  validators=[MinValueValidator(-180), MaxValueValidator(180)])
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

# ---------- Additional User Attributes ------------
class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username