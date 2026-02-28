from django.http import HttpResponse
from django.shortcuts import render
from store.models import Products


def home (request):
    products = Products.objects.filter(is_available=True)
    context={
        "product":products
    }
    return render(request,"index.html",context)