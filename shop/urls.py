from django.urls import path
from .views import *

urlpatterns = [
    path('', item_list, name='item_list'),
    path('checkout/', checkout_page, name='checkout_page'),
    path('product/', product_page, name='product_page'),
    ]