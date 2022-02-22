from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import *

class PropertySerializer(ModelSerializer):
    class Meta:
        model = Property
        fields = '__all__'
        