from django.urls import path 
from .views import products ,product,products_by_category

urlpatterns = [
    path('' , products , name='products'),
    path('product-details/<int:id>/' , product , name='product-details'),
    path('category/<str:category>/' , products_by_category , name=' products_by_category'),
]
