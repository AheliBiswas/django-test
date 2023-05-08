from django.urls import path
from . import views
urlpatterns = [
    path('',views.customerPage,name='customer'),
    path('address/',views.addressPage,name='address'),
    path('cars/',views.carsPage,name='cars')
]
