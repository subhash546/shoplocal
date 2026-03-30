from django.shortcuts import render
from .models import Products
from category.models import Category
from django.shortcuts import get_object_or_404
from cart.models import CartItem
from cart.views import _card_id
from django.http import HttpResponse
from django.db.models import Q
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

# Create your views here.

def store(request,slug=None):
    categories=None
    products=None
    
    if slug!=None:
       categories= get_object_or_404(Category,slug=slug)
       products=Products.objects.filter(category=categories,is_available=True)
       paginator=Paginator(products,4)
       page=request.GET.get('page')
       page_obj=paginator.get_page(page)
       product_count=products.count()
    else:
    
       products = Products.objects.filter(is_available=True)
       paginator=Paginator(products,6)
       page=request.GET.get('page')
       page_obj=paginator.get_page(page)
       
       
       product_count=products.count()
    context={
        "product":page_obj,
        "product_count":product_count
    }
    
    return render(request,"store/store.html",context)
 
 
 
def product(request,category_slug,product_slug):
   products=get_object_or_404(Products,slug=product_slug, category__slug=category_slug)
   in_cart=CartItem.objects.filter(cart__cart_id=_card_id(request),product=products).exists()
   
   context={
      "product":products,
      "in_cart":in_cart
   }
   print(context)
    
    
   return render(request,"store/product_details.html",context)



def search(request):
    keyword = ''
    products = Products.objects.none()  # safer default

    if 'keyword' in request.GET:
        keyword = request.GET['keyword'].strip()
        print("Keyword value:", keyword)

        if keyword:  # only search if not empty
            products = Products.objects.filter(
                Q(product_name__icontains=keyword) |
                Q(description__icontains=keyword),
                is_available=True
            )
            product_count=products.count()

    context = {
        'product': products,
        'keyword': keyword,
         "product_count":product_count
    }

    print(products.query)  # debug SQL
    return render(request, "store/store.html", context) 
