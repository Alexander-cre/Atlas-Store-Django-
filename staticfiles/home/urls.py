from django.urls import path 
from .views import index ,aboutPage,client,contact

urlpatterns = [
    path('' , index, name='home'),
    path('aboutus/', aboutPage, name='aboutus'),
    path('client/', client, name='client'),
    path('contact/', contact, name='contact'),
]
