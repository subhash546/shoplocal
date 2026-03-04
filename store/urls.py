

from django.urls import path
from .views import store,product


urlpatterns = [
    path('',store,name="store"),
    path('<slug:slug>/',store,name="category_name"),
    path('<slug:category_slug>/<slug:product_slug>/', product, name='product_detail'),
    


]
