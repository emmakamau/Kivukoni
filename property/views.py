
from unicodedata import category
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from property.forms import *
from .models import *
from .filters import *
import folium
from folium import plugins

# Create your views here.


def home(request):

    property = Property.objects.all().filter(status='Onsale')[:6]
    property_list = Property.objects.values_list('latitude', 'longitude')
    myMap = folium.Map(zoom_start=2, min_zoom=3)

    for i in property_list:
        folium.Marker(i).add_to(myMap)

    myMap = myMap._repr_html_()


    context = {
        'property': property,
        'myMap':myMap,
    }
    return render(request, 'property/index.html', context=context)


def administrator(request):
    
    
    context = {

    }
    return render(request, 'property/administrator.html', context)


def propertylist(request):

    property = Property.objects.all()
    property_list = Property.objects.values_list('latitude', 'longitude')

    myMap = folium.Map(zoom_start=1, min_zoom=2)

    for i in property_list:
        folium.Marker(i).add_to(myMap)

    myMap = myMap._repr_html_()

    myFilter = PropertyFilter(request.GET, queryset=property)
    property = myFilter.qs
    property_count = property.count()

    paginator = Paginator(property, 3) # Show 3 property items per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'property': property,
        'myFilter': myFilter,
        'property_count': property_count,
        'myMap': myMap,
        'page_obj':page_obj,
    }
    return render(request, 'property/propertylist.html', context=context)

def propertytype(request):

    type = Propertytype.objects.all()
    print(type)

    context = {
        'type':type,
    }
    return render(request, 'property/propertytype.html', context=context)

def propertyitem(request, id):

    property_obj = Property.objects.get(id=id)
    image = Images.objects.filter(property=property_obj)

    lat = property_obj.latitude
    lng = property_obj.longitude

    myMap = folium.Map(location=[lat, lng], zoom_start=100)
    folium.Marker([lat, lng]).add_to(myMap)
    myMap = myMap._repr_html_()

    context = {
        'property_obj': property_obj,
        'myMap': myMap,
        'image': image
    }
    return render(request, 'property/propertypage.html', context=context)


def regionfilter(request):
    property = Property.objects.all().filter()

    context = {
        'property': property,
    }
    return render(request, 'property/propertylist.html', context=context)
