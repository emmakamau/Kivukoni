import django_filters
from .models import *
from django_filters import *

class PropertyFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name='price', lookup_expr='lte')
    
    class Meta:
        model = Property
        fields = '__all__'
        exclude = ['image','title','description','uploaddate','address','price','longitude','latitude']