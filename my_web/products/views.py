
from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from django.contrib import messages

# Create your views here.
def product_detail (request, pk):
    categories = Category.objects.all()
    product = get_object_or_404 (Product, pk=pk)
        
    # related_products = Product.objects.filter(category = product.category). exclude (pk=pk)
    context = {
        'product' : product,
        'categories' : categories,
    }
    return render (request, 'products/product_detail.html', context)

def product_category (request, pk): 
    categories = Category.objects.all()
    category = get_object_or_404(Category, pk =pk)
    products = Product.objects.filter(category = category)
    context = {
            'products': products,
            'categories' : categories,
    }
    return render (request, 'core/index.html', context)
def search(request):  
    categories = Category.objects.all()  
    query = request.GET.get('q')  
    if query:  
        products = Product.objects.filter(name__icontains=query)  
        if products is not None:  
            count = products.count  
            context = {  
            'products': products,  
            'categories': categories,  
            'count': count ,
            'query' : query
            }  
            return render(request, 'products/store.html', context)  
        else:  
            messages.error(request, "No products found")  
    else:  
        products = Product.objects.all()  
    count = products.count
    
    return render(request, 'products/store.html', context)