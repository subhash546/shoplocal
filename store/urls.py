

from django.urls import path
from .views import store,product,search


urlpatterns = [
    path('',store,name="store"),
    path('category/<slug:slug>/',store,name="category_name"),
    path('category/<slug:category_slug>/<slug:product_slug>/', product, name='product_detail'),
    path('search/',search,name="search"),
    


]
