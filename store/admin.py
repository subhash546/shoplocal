from django.contrib import admin

from .models import Products

# Register your models here.

class ProductModel(admin.ModelAdmin):
    prepopulated_fields={'slug':('product_name',)}
    list_display=('product_name','price','stocks','created_at','updated_at')
    
    
admin.site.register(Products,ProductModel)
