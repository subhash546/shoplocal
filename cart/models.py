from django.db import models
from store.models import Products,Variations

# Create your models here


class Cart(models.Model):
    cart_id=models.CharField(max_length=250)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.cart_id
    
    
class CartItem(models.Model):
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    variations=models.ManyToManyField(Variations,blank=True)
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    is_active=models.BooleanField(default=True)
    
    def sub_total(self):
        return self.product.price * self.quantity
    
    def __str__(self):
      return self.product.product_name