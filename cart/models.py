from products.models import Product
from django.db import models

class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # Link to the product
    quantity = models.IntegerField(default=1)  # Quantity of the product in the cart
    created_at = models.DateTimeField(auto_now_add=True)  # When the item was added to the cart
    updated_at = models.DateTimeField(auto_now=True)  # When the item was last updated

    def __str__(self):
        return f"{self.product.name} (x{self.quantity})"