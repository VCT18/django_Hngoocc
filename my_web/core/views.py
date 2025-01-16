from django.shortcuts import render

from products.models import Category, Product 
def index(request):
    categories = Category.objects.all() 
    products = Product.objects.all()
    products_on_sale = Product.objects.filter(on_sale=True)

    context = {
        'categories': categories,
        'products_on_sale' : products_on_sale,
        'products': products
    }
    
    return render(request, 'core/index.html', context)

def about(request):
    categories = Category.objects.all() 
    products = Product.objects.all()
    context = {
        'categories': categories,
        'products': products
    }
    return render(request, 'core/about.html', context)

def contact(request):
    categories = Category.objects.all() 
    products = Product.objects.all()
    context = {
        'categories': categories,
        'products': products
    }
    return render(request, 'core/contact.html',context)
