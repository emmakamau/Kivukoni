from unittest.util import _MAX_LENGTH
from django.db import models
import geocoder

# Create your models here.
class Propertytype(models.Model):
    name = models.CharField(max_length=255)
    demoimage = models.ImageField(blank=False, null=False, upload_to='media', default=0)

    class Meta:
        verbose_name_plural = 'Property Type'

    def __str__(self):
        return self.name

class Region(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Region'

    def __str__(self):
        return self.name

class Location(models.Model):
    region = models.ForeignKey('Region',on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Location'

    def __str__(self):
        return self.name

class Currency(models.Model):
    name = models.CharField(max_length=3)

    class Meta:
        verbose_name_plural = 'Currency'

    def __str__(self):
        return self.name

class Property(models.Model):
    STATUS = (
        ('Onsale', 'Onsale'),
        ('Sold', 'Sold'),
        ('Reserved', 'Reserved'),
    )
    propertytype = models.ForeignKey('Propertytype',on_delete=models.SET_NULL, null=True)
    image = models.ImageField(blank=False, null=False, upload_to='media', default=0)
    region = models.ForeignKey('Region',on_delete=models.SET_NULL, null=True)
    location = models.ForeignKey('Location',on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200, null=True)
    currency = models.ForeignKey('Currency',on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    title = models.CharField(max_length=510)
    description = models.TextField(max_length=10000)
    uploaddate = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=50, null=True, choices=STATUS)
    latitude = models.FloatField(default=0, null=True, blank=True)
    longitude = models.FloatField(default=0, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.latitude = geocoder.osm(self.address).lat
        self.longitude = geocoder.osm(self.address).lng
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Property Log'
    
    

class Images(models.Model):
    image = models.ImageField(blank=False, null=False, upload_to='media')
    property = models.ForeignKey('Property',on_delete=models.SET_NULL, null=True )

    class Meta:
        verbose_name_plural = 'Images'
