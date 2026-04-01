from django.db import models
from category.models import Category
from django.urls import reverse

# Create your models here.

class Products(models.Model):
    product_name=models.CharField(max_length=50,unique=True,blank=False)
    slug=models.SlugField(max_length=100,unique=True)
    description=models.TextField(max_length=250,blank=True)
    price=models.IntegerField()
    is_available=models.BooleanField(default=True)
    stocks=models.IntegerField()
    photo=models.ImageField(upload_to='photos/product')
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    
    def get_url(self):
        return reverse("product_detail" ,args=[self.category.slug,self.slug])
    
    
       
    def __str__(self):
        return self.product_name
    
    

    
variations_category_choices=(
        ('color','Color'),
        ('size','Size')
    )
    
    
class Variations(models.Model):
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    variation_category=models.CharField(max_length=100,choices=variations_category_choices)
    variation_value=models.CharField(max_length=100)
    is_active=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
     return f"{self.product.product_name} - {self.variation_value}"
    
    
    
    
    
    
