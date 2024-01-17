from django.db import models
from django_countries.fields import CountryField
from phone_field import PhoneField
# Create your models here.
class MyApiModel(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    # phone=PhoneField(blank=True,help_text='contact phone number')
    dob=models.DateField(auto_now=False,auto_now_add=False)
    country=CountryField()
    def __str__(self):
        return self.name
    
