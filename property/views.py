from locale import currency
from os import stat
from pydoc import locate
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .filters import *
import folium
from folium import plugins

# Create your views here.


def home(request):

    property = Property.objects.all().filter(status='Onsale')[:6]
    property_list = Property.objects.values_list('latitude', 'longitude')

    myMap = folium.Map(zoom_start=10)

    for i in property_list:
        folium.Marker(i).add_to(myMap)

    myMap = myMap._repr_html_()


    context = {
        'property': property,
        'myMap':myMap,
    }
    return render(request, 'property/index.html', context=context)


def administrator(request):

    region = Region.objects.all()
    currency = Currency.objects.all()
    location = Location.objects.all()
    propertytype = Propertytype.objects.all()
    status = Property.objects.values_list('status').distinct()

    if request.method == 'POST':
        data = request.POST
        images = request.FILES.getlist('images')
        
        if data['region'] != 'none':
            if data['location'] != 'none':
                if data['currency'] != 'none':
                    if data['propertytype'] != 'none':
                        if data['status'] != 'none':
                            region = Region.objects.get(id=data['region'])
                        location = Location.objects.get(id=data['location'])
                    currency = Currency.objects.get(id=data['currency'])
                propertytype = Propertytype.objects.get(id=data['propertytype'])
            status = Property.objects.values.get(id=data['status'])
        else:
            currency = None
            location = None
            region = None
            propertytype = None
            status = None

        for image in images:
            Property.objects.create(
                title=data['title'],
                region=region,
                location=location,
                currency=currency,
                propertytype = propertytype,
                description=data['description'],
                status=status,
                address=data['address'],
                price=data['price'],
                image=image,
            )
            print(property)

        return redirect('propertylist')

    context = {
        'region': region,
        'currency': currency,
        'location': location,
        'propertytype':propertytype,
        'status':status,
    }
    return render(request, 'property/administrator.html', context)


def propertylist(request):

    property = Property.objects.all()
    property_list = Property.objects.values_list('latitude', 'longitude')

    myMap = folium.Map(zoom_start=100)

    for i in property_list:
        folium.Marker(i).add_to(myMap)

    myMap = myMap._repr_html_()

    myFilter = PropertyFilter(request.GET, queryset=property)
    property = myFilter.qs
    property_count = property.count()

    context = {
        'property': property,
        'myFilter': myFilter,
        'property_count': property_count,
        'myMap': myMap,
    }
    return render(request, 'property/propertylist.html', context=context)


def propertyitem(request, id):
    property = Property.objects.get(id=id)
    lat = property.latitude
    lng = property.longitude
    print(lat, lng)

    myMap = folium.Map(location=[lat, lng], zoom_start=100)
    folium.Marker([lat, lng]).add_to(myMap)
    myMap = myMap._repr_html_()

    context = {
        'property': property,
        'myMap': myMap,
    }
    return render(request, 'property/propertypage.html', context=context)


def regionfilter(request):
    property = Property.objects.all().filter()

    context = {
        'property': property,
    }
    return render(request, 'property/propertylist.html', context=context)
