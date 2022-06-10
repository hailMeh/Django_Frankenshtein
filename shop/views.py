from django.shortcuts import render
from .models import *
# Create your views here.


def item_list(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, 'shop/home-page.html', context)


def checkout_page(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, 'shop/checkout-page.html', context)

def product_page(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, 'shop/product-page.html', context)
