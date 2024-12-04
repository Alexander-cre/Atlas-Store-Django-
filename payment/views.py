# views.py

from django.shortcuts import render, redirect
from .paypal import paypalrestsdk
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def create_payment(request):
    if request.method == "POST":
        # Create a payment object
        payment = paypalrestsdk.Payment({
            "intent": "sale",
            "payer": {
                "payment_method": "paypal"
            },
            "redirect_urls": {
                "return_url": request.build_absolute_uri('/payment/execute/'),
                "cancel_url": request.build_absolute_uri('/cart/')
            },
            "transactions": [{
                "item_list": {
                    "items": [{
                        "name": "Item Name",  # Replace with actual item name
                        "sku": "item",
                        "price": "10.00",  # Replace with actual item price
                        "currency": "EUR",
                        "quantity": 1
                    }]
                },
                "amount": {
                    "total": "10.00",  # Replace with actual total amount
                    "currency": "EUR"
                },
                "description": "This is the payment description."
            }]
        })

        # Create the payment
        if payment.create():
            print("Payment created successfully")
            for link in payment.links:
                if link.rel == "approval_url":
                    return redirect(link.href)
        else:
            print(payment.error)
    
    return render(request, 'cart.html')

# views.py (continued)

@csrf_exempt
def execute_payment(request):
    payment_id = request.GET.get('paymentId')
    payer_id = request.GET.get('PayerID')

    payment = paypalrestsdk.Payment.find(payment_id)

    if payment.execute({"payer_id": payer_id}):
        print("Payment executed successfully")
        # Handle post-payment actions, like clearing the cart, sending confirmation, etc.
        return redirect('payment_success')  # Redirect to a success page
    else:
        print(payment.error)  # Handle payment failure
        return redirect('payment_failure')  # Redirect to a failure page