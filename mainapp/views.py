from django.shortcuts import render
from products.models import ProductsCategory, Products

# Create your views here.

def index(request):
    
    productsCategory = ProductsCategory.objects.all()
    products = Products.objects.all()
    
    return render(request, 'mainapp/index.html', {
        'title': 'home',
        'productsCategory': productsCategory,
        'products': products
    })
    
def login(request):
    
    return render(request, 'mainapp/login.html', {
        'title': 'Login'
    })