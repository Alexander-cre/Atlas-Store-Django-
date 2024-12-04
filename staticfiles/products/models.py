from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    # Info of Product
    name = models.CharField(max_length=255) 
    price = models.DecimalField(max_digits=10,decimal_places=2)
    description = models.TextField(max_length=300) # Limit to 300 words max
    size = models.CharField(max_length=100,help_text="Enter sizes seperates by commas, e.g S,M,L") # Stores sizes such as M, L, S, XL, XXl
    quantity = models.IntegerField()
    SKU = models.CharField(max_length=100, unique=True)  
    # Images of Product at which to save space onthe DB images used would have to be by links
    Image1 = models.TextField()
    Image2 = models.TextField()
    Image3 = models.TextField()
    Image4 = models.TextField()
    # Category
    category = models.ForeignKey(Category, on_delete=models.CASCADE) # Products WIll be displayed by their Category 
    # Time Signatures
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name