from django.db import models

# Create your models here.

class Product(models.Model):

# Allows user to select the choice of their caegory to funnel the search

    # Info of Product
    name = models.CharField(max_length=255) 
    price = models.DecimalField(max_digits=10,decimal_places=2)
    description = models.TextField(max_length=2000) # Limit to 300 words max
    quantity = models.IntegerField()
    SKU = models.CharField(max_length=200)  
    # Images of Product at which to save space onthe DB images used would have to be by links
    Image = models.TextField()

    # Category
    category = models.CharField(max_length=200) # Products WIll be displayed by their Category 
    # Time Signatures
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name