from django.shortcuts import render

from products.models import Category, Product 
def index(request):
    categories = Category.objects.all() 
    products = Product.objects.all()
    context = {
        'categories': categories,
        'products': products
    }
    
    return render(request, 'core/index.html', context)

def about(request):
    return render(request, 'core/about.html')

def contact(request):
    return render(request, 'core/contact.html')