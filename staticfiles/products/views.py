from django.shortcuts import render , get_object_or_404
from .models import Product, Category

#  List all Products
def products(request):
    product_list = Product.objects.all()
    return render(request, 'catalogs/catalog.html' , {'products': product_list}) 

# Gets a single Product by ID
def product(request, id):
    product_info = get_object_or_404(Product, id=id)
    return render(request, 'productDetails/product.html',{'product':product_info})

# Gets a list of products by their Category
def products_by_category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    product_list_cat = Product.objects.filter(category=category) # filters a product by the Category property in the product
    return render(request, 'catalogs/products.html', {'category': category})
