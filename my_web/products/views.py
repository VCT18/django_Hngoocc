
from django.shortcuts import render, get_object_or_404
from .models import Category, Product
# Create your views here.
def product_detail (request, pk):
    categories = Category.objects.all()
    product = get_object_or_404 (Product, pk=pk)
        
    # related_products = Product.objects.filter(category = product.category). exclude (pk=pk)
    context = {
        'product' : product,
        'categories' : categories,
    }
    return render (request, 'core/index.html', context)

def product_category (request, pk): 
    categories = Category.objects.all()
    category = get_object_or_404(Category, pk =pk)
    products = Product.objects.filter(category = category)
    context = {
            'products': products,
            'categories' : categories,
    }
    return render (request, 'core/index.html', context)