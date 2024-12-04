from django.conf import settings
from django.shortcuts import render ,redirect , get_object_or_404
from django.http import HttpResponse 
from .cart import CartManager 
from .models import Product 

# Create your views here.
# All Cart Items
def cart_detail(request):
    cart_manager = CartManager(request)
    cart_items = cart_manager.get_items()
    total_items = cart_manager.get_total_items()
    grand_total = cart_manager.get_total_price()
    return render(request , 'cart/Cart.html', {'cart_manager': cart_manager , 'cart_items': cart_items, 'total_items': total_items,'grand_total': grand_total })

# Add item to Cart Function
def cart_add(request, product_id):
    cart = CartManager(request)
    product = get_object_or_404(Product , id=product_id)
    print(type(product),product)
    # Gets Quantity from the user 
    quantity = int(request.POST.get('quantity', 1))
    # Get size from the user if noneadded
    size = request.POST.get('size', None)
    # The add product to cart with the specified Quantity 
    cart.add(product_id=product_id , quantity=quantity, size=size)
    return redirect('cart:cart_detail') 

# Remove from Cart Function
def cart_remove(request, product_id,size=None):
    cart = CartManager(request)
    product = get_object_or_404(Product,id=product_id)
    cart.remove(product_id,size)
    return redirect('cart_detail')

# Clears all 
def cart_clear(request):
    cart_manager = CartManager(request)
    cart_manager.clear()
    return redirect('cart:cart_detail')