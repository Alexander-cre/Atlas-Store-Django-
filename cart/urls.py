from django.urls import path
from .views import add_to_cart, view_cart, update_cart, remove_from_cart , successpay

app_name = 'cart' 

urlpatterns = [
    path('cart/add/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('', view_cart, name='view_cart'),
    path('cart/update/<int:product_id>/', update_cart, name='update_cart'),
    path('cart/remove/<int:product_id>/', remove_from_cart, name='remove_from_cart'),
    path('success/' , successpay , name='successpay'),
]