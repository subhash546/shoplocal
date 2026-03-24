

from django.urls import path



from .views import cart,add_cart,minus_cart,removecart

urlpatterns = [
    path('', cart,name="cart"),
    path('add_cart/<int:product_id>/',add_cart,name="addcart"),
    path('sub_cart/<int:product_id>/',minus_cart,name="subcart"),
    path('remove_cart/<int:product_id>/',removecart,name="removecart"),
     
]
