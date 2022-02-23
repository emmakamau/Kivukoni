from django.contrib import admin
from .models import *


class PropertyAdmin(admin.ModelAdmin):
    list_display = ('title','propertytype','region','location',
    'address','currency','status')

class LocationAdmin(admin.ModelAdmin):
    list_display = ('region', 'name')

class ImageAdmin(admin.ModelAdmin):
    list_display=('property', 'image')


# Register your models here.
admin.site.register(Propertytype)
admin.site.register(Property, PropertyAdmin)
admin.site.register(Currency)
admin.site.register(Region)
admin.site.register(Location, LocationAdmin)
admin.site.register(Images, ImageAdmin)