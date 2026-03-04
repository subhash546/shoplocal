from django.shortcuts import render
from .models import Products
from category.models import Category
from django.shortcuts import get_object_or_404

# Create your views here.

def store(request,slug=None):
    categories=None
    products=None
    
    if slug!=None:
       categories= get_object_or_404(Category,slug=slug)
       products=Products.objects.filter(category=categories,is_available=True)
       product_count=products.count()
    else:
    
       products = Products.objects.filter(is_available=True)
       product_count=products.count()
    context={
        "product":products,
        "product_count":product_count
    }
    
    return render(request,"store/store.html",context)
 
 
 
def product(request,category_slug,product_slug):
   products=get_object_or_404(Products,slug=product_slug, category__slug=category_slug)
   context={
      "product":products
   }
   print(context)
    
    
   return render(request,"store/product_details.html",context)
