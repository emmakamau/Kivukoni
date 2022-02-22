from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Propertytype)
admin.site.register(Property)
admin.site.register(Currency)
admin.site.register(Region)
admin.site.register(Location)
#admin.site.register(Status)