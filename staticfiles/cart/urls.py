from django.urls import path
from . import views

app_name = 'cart'   #Declaring namespace

urlpatterns = [
    path('' , views.cart_detail , name='cart_detail') ,
    # Add to Cart
    path('add/<int:product_id>/' , views.cart_add , name='cart_add') ,
    # Remove from Cart
    path('remove/<int:product_id>/<str:size>/' , views.cart_remove , name='cart_remove') ,
    # Clear all from Cart
    path('cart/clear/' , views.cart_clear , name='cart_clear') ,


]