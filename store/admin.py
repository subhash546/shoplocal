from django.contrib import admin

from .models import Products,Variations

# Register your models here.

class ProductModel(admin.ModelAdmin):
    prepopulated_fields={'slug':('product_name',)}
    list_display=('product_name','price','stocks','category','created_at','updated_at')
    
    
class VariationsModel(admin.ModelAdmin):
    list_display = ('product', 'variation_category', 'variation_value', 'is_active', )
    list_editable = ('is_active',)
    list_filter = ('product', 'variation_category', 'variation_value', 'is_active', )
    
    
admin.site.register(Products,ProductModel)
admin.site.register(Variations,VariationsModel)
