# urls.py

from django.urls import path
from .views import create_payment, execute_payment

app_name = 'payment'

urlpatterns = [
    path('payment/create/', create_payment, name='create_payment'),
    path('payment/execute/', execute_payment, name='execute_payment'),
    # Add other paths as needed
]