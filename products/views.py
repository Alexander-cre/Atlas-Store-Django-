from django.shortcuts import render
from .models import Product  # Assuming you have a Product model

def products(request):
    products = Product.objects.all()  # Fetch all products from the database
    return render(request, 'home/index.html', {'products': products})

def get_product_by_id(product_id):
    try:
        return Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return None  # Return None if the product does not exist