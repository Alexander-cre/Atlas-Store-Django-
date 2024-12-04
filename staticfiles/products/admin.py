from django.contrib import admin
from .models import Product , Category

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ( 'name','price','category','quantity','SKU')
    list_filter = ('category',)
    search_fields = ('name','sku')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)    
