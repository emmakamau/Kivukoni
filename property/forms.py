from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *

class PropertyForm(ModelForm):
    class Meta:
        model = Property
        fields = ['region','location','address','currency','price',
        'title','description','status']

'''
properttype = models.ForeignKey('Propertytype',on_delete=models.SET_NULL, null=True)
    image = models.ImageField(blank=False,null=False,upload_to='media')
    region = models.ForeignKey('Region',on_delete=models.SET_NULL, null=True)
    location = models.ForeignKey('Location',on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200, null=True)
    currency = models.ForeignKey('Currency',on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    title = models.CharField(max_length=510)
    description = models.TextField(max_length=10000)
    uploaddate = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=50, null=True, choices=STATUS)
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)
'''
