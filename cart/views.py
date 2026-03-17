from django.shortcuts import render,get_object_or_404,redirect
from .models import Products,Cart,CartItem

# Create your views here.

def cart(request):
    return render(request,"store/cart/cart.html")

def _card_id(request):
    cart=request.session.session_key
    
    if not cart:
        cart=request.session.create()
    return cart 

def add_cart(request,product_id):
    product=get_object_or_404(Products,id=product_id)
    try:
        cart =Cart.objects.get(cart_id=_card_id(request))
        
    except Cart.DoesNotExist:
        cart=Cart.objects.create(
            cart_id=_card_id(request)
        )
        cart.save()
        
    try:
        cart_item=CartItem.objects.get(product=product,cart=cart)
        cart_item.quantity+=1
        cart_item.save()
        
    except CartItem.DoesNotExist:
        cart_item=CartItem.objects.create(
            cart=cart,
            product=product,
            quantity=1
        )
        cart_item.save()
    return redirect('cart')
    