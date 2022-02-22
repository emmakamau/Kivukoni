from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('property/', views.propertylist, name="propertylist"),
    path('property/<str:id>/', views.propertyitem, name="propertyitem"),

    path('administrator/',views.administrator, name="administrator")

]