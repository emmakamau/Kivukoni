from django.forms import ModelForm
from django import forms
from django.forms import fields, widgets
from .models import *

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['propertytype','image','region','location','address','currency',
        'price','title','description','status','latitude','longitude']

        widgets={
            'propertytype':widgets.Select(attrs={
                'class':'form-control',
                'placeholder':'Select a property type...',
                'id':'propertytype'
            }),
            'region':widgets.Select(attrs={
                'class':'form-control',
                'placeholder':'Select a region...',
                'id':'region'
            }),
            'location':widgets.Select(attrs={
                'class':'form-control',
                'placeholder':'Select a location...',
                'id':'location'
            }),
            'address':widgets.Input(attrs={
                'class':'form-control',
                'placeholder':'Enter a detailed address...',
                'id':'address'
            }),
            'currency':widgets.Select(attrs={
                'class':'form-control',
                'placeholder':'Select type of currency...',
                'id':'currency'
            }),
            'price':widgets.NumberInput(attrs={
                'class':'form-control',
                'placeholder':'Price',
                'id':'price'
            }),
            'title':widgets.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Property Title e.g Spacious one bedroom apartment near UoN.',
                'id':'title'
            }),
            'description':widgets.Textarea(attrs={
                'class':'form-control',
                'placeholder':'Enter a description...',
                'rows':'8',
                'id':'description'
            }),
            'status':widgets.RadioSelect(attrs={
                'class':'form-control',
                'id':'status'
            }),
            'longitude':widgets.NumberInput(attrs={
                'class':'form-control',
                'placeholder':'Enter property Longitude',
                'id':'longitude'
            }),
            'latitude':widgets.NumberInput(attrs={
                'class':'form-control',
                'placeholder':'Enter property Latitude',
                'id':'latitude'
            })
        }

