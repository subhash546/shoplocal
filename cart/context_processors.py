from .models import Cart,CartItem
from .views import _card_id

def counter(request):
    cart_counter=0
    # Skip for admin panel
    if request.path.startswith('/admin'):
        return {}
    else:
        try:
            cart=Cart.objects.get(cart_id=_card_id(request))
            cart_items=CartItem.objects.filter(cart=cart,is_active=True)
            for i in cart_items:
                cart_counter+=i.quantity
        except Cart.DoesNotExist:
            cart_counter=0
    return dict(cart_counter=cart_counter)
            
            
            