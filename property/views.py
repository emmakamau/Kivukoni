from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .decorators import unauthenticated_user
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
        'myMap': myMap,
    }
    return render(request, 'property/index.html', context=context)

@unauthenticated_user
def loginuser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('administrator')
        else:
            messages.info(request, "Username or Password is incorrect")
            
    context = {}
    return render (request, 'property/login.html', context=context)

@login_required
def logoutuser(request):
    logout(request)
    return render(request,'property/index.html',context=context)

@login_required
def administrator(request):
    property_type = Propertytype.objects.all()
    regions = Region.objects.all()
    location = Location.objects.all()
    currency = Currency.objects.all()
    property = Property.objects.all()


    context = {
        'property_type':property_type,
        'regions':regions,
        'location':location,
        'currency':currency,
        'property':property,
    }

    return render(request,'property/admin.html',context=context)

@login_required
def admin_property_type(request):
    context={}

    return render(request,'property/admin-propertytype.html', context=context)

@login_required
def admin_images(request):
   
    property=Property.objects.all()

    if request.method == 'POST':
        data = request.POST
        images = request.FILES.getlist('images')
        if data['property'] != 'none':
            property = Property.objects.get(id=data['property'])
        print(images, property)

        for image in images:
            images = Images.objects.create(
                property=property,
                image=image
            )
            return redirect('home')

    context={'property':property}

    return render(request,'property/admin-images.html', context=context)

@login_required
def admin_currency(request):
    if request.method == 'POST':
        currency = request.POST.get('currency')

        Currency.objects.create(
            name=currency
        )
        return redirect('administrator')

    context={}

    return render(request,'property/admin-currency.html', context=context)

@login_required
def admin_region(request):
    if request.method == 'POST':
        region = request.POST.get('region')

        Region.objects.create(
            name=region
        )
        return redirect('administrator')
    context={}

    return render(request,'property/admin-region.html',context=context)

@login_required
def admin_location(request):
    
    region = Region.objects.all()

    if request.method == 'POST':
        data = request.POST
        location = request.POST.get('location')
        if data['region'] != 'none':
            region = Region.objects.get(id=data['region'])

            Location.objects.create(
                name=location,
                region=region
            )
            return redirect('administrator')
        
    context={
        'region': region,
    }

    return render(request,'property/admin-location.html',context=context)

def propertylist(request):

    type = request.GET.get('type')
    region = request.GET.get('region')

    if type == None:
        property = Property.objects.all().order_by('status')
    else:
        property = Property.objects.all().filter(propertytype__name=type)

    property_list = Property.objects.values_list('latitude', 'longitude')

    myMap = folium.Map(zoom_start=1, min_zoom=2)

    for i in property_list:
        folium.Marker(i).add_to(myMap)

    myMap = myMap._repr_html_()

    myFilter = PropertyFilter(request.GET, queryset=property)
    property = myFilter.qs
    property_count = property.count()

    paginator = Paginator(property, 3)  # Show 3 property items per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'property': property,
        'myFilter': myFilter,
        'property_count': property_count,
        'myMap': myMap,
        'page_obj': page_obj,
    }
    return render(request, 'property/propertylist.html', context=context)


def propertytype(request):

    type = Propertytype.objects.all()

    context = {
        'type': type,
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


def contactus(request):

    if request.method == 'POST':
        name = request.POST.get('user-name')
        email = request.POST.get('email')
        msg = request.POST.get('message')

        print(name,email,msg)

        from_email = email
        recipient_list = 'emmaculatewkamau@gmail.com'
        subject = 'Enquiry'
        greetings = 'Dear sir,\n\n'
        closing = 'Thank you.\n'
        message = greetings+msg+'\n\n'+closing+name

        try:
            send_mail(subject, message, from_email, [recipient_list])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return redirect('home')

    context={}
    return render(request, 'property/contactus.html', context=context)