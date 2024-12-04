from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from decimal import Decimal


def get_product_by_id(product_id):
    try:
        return Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return None

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    
    # Get the cart from the session
    cart = request.session.get('cart', {})
    
    # If the product is already in the cart, increase the quantity
    if str(product.id) in cart:
        cart[str(product.id)] += 1
    else:
        cart[str(product.id)] = 1
    
    # Save the updated cart back to the session
    request.session['cart'] = cart
    return redirect('cart:view_cart')

def view_cart(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total_price = Decimal('0.00')  # Initialize total_price as Decimal
    shipping_cost = Decimal('2.00')  # Fixed shipping cost as Decimal

    for product_id, quantity in cart.items():
        product = get_product_by_id(product_id)
        if product:
            item_total_price = product.price * quantity  # product.price should be Decimal
            total_price += item_total_price  # Add to total price
            cart_items.append({
                'product': product,
                'quantity': quantity,
                'total_price': item_total_price,
            })

    total_price += shipping_cost  # Add shipping cost to total price

    context = {
        'cart_items': cart_items,
        'total_price': total_price,  # Pass the total price including shipping to the context
        'shipping_cost': shipping_cost,  # Optionally pass the shipping cost to the context
    }
    return render(request, 'cart/Cart.html', context)

def update_cart(request, product_id):
    cart = request.session.get('cart', {})
    
    if str(product_id) in cart:
        if request.method == 'POST':
            action = request.POST.get('action')
            if action == 'increment':
                cart[str(product_id)] += 1  # Increment the quantity
            elif action == 'decrement':
                if cart[str(product_id)] > 1:
                    cart[str(product_id)] -= 1  # Decrement the quantity
                else:
                    del cart[str(product_id)]  # Remove item if quantity is 0
            request.session['cart'] = cart
            return redirect('cart:view_cart')
    
    return redirect('view_cart')

def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    
    if str(product_id) in cart:
        del cart[str(product_id)]  # Remove the item from the cart
    
    request.session['cart'] = cart
    return redirect('cart:view_cart')

def successpay(request):
    return render(request, 'cart/success.html')