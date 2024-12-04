from decimal import Decimal
from django.conf import settings
import cart
from products.models import Product #imports the model of products from the products section
from .models import Cart,CartItem

# Here ill manage Cart session since i dont want to be creating a new cart for each user

class CartManager:
    def __init__(self, request):
        self.request = request # add session in th cart 
        self.session = request.session  # add session in th cart
        self.cart = self.session.get(settings.CART_SESSION_ID, {}) # add session in th cart


        if settings.CART_SESSION_ID in self.session:   
            self.cart = self.session[settings.CART_SESSION_ID] 
                
        else:
            # Saves an empty cart in session
            self.cart = self.session[settings.CART_SESSION_ID] = {} # add in the session as an array
           
# Add to Cart Function ( with Quantity and Size )
    def add(self, product_id , quantity=1, size=None , update_quantity=False):

        product = Product.objects.get(id=product_id)

        key =f"{product_id}:{size}"

        if key not in self.cart:
            self.cart[key] ={
                'quantity':0,
                 'price':str(product.price),
                 'size' : size,
                 'name': product.name,
                 'category' : product.category.name
                }
            if update_quantity :
                self.cart[key]['quantity'] = quantity
            else :
                self.cart[key]['quantity'] = quantity

                # Update the size if its provided

            if size:
                self.cart[key]['size'] = size

            # Save Cart back into session
            self.save()
            print(cart.cart)

    def save(self):
        # Marks the session as modified to ensure it gets saved
        self.session[settings.CART_SESSION_ID] = self.cart
        self.request.session.modified = True
        print("Cart items : ", self.cart)

# Remove from Cart function 
    def remove(self, product_id):
        key = str(product_id)
        if key in self.cart:
            del self.cart[key] # Delete Operator in PY
            self.save()

    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)

        for product in products:
            cart_item = self.cart[str(product.id)]
            cart_item['product']=product
            cart_item['total_price'] = Decimal(cart_item['price']) * cart_item['quantity']
            yield cart_item

# Get the total Price in Cart
    def get_total_price(self):
        grand_total = 0         
        # Ensiuring that i seperate ID from SIZE 
        for key,item in self.cart.items():
            product_id=key.split(':')[0]
            product = Product.objects.get(id=product_id)
            #  Using the Exracted ID

            grand_total += item['quantity'] * float(item['price'])
            return grand_total
    
# Gets all the items in the cart
    def get_items(self):
        # Ensiuring that i seperate ID from SIZE 
        product_ids = [int(key.split(':')[0])
        for key in self.cart.keys()]
        
        products = Product.objects.filter(id__in = product_ids)
        cart_items = []
        for product in products:
            product_id_str = str(product.id)
            if product_id_str in self.cart:
                item = {
                    'product' : product,
                    'quantity': self.cart[product_id_str]['quantity'],
                    'size': self.cart[product_id_str]['size'],
                    'total_price': product.price * self.cart[product_id_str]['quantity'],
                }

                cart_items.append(item)
                return cart_items


# Gets the total number of items in the cart
    def get_total_items(self):
        return sum(item['quantity']
                   for item in self.cart.values())

# Clear all items in Cart
    def clear(self):
        self.session[settings.CART_SESSION_ID]  = {}
        self.session.modified =True    

