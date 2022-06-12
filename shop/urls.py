from django.urls import path
from .views import *

urlpatterns = [
    path('', ItemList.as_view(), name='ItemList'),
    path('checkout/', checkout_page, name='checkout_page'),
    path('product/<slug:slug>/', ItemDetail.as_view(), name='ItemDetail'),
    path('add_to_cart/<slug>/', add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<slug>/', remove_from_cart, name='remove_from_cart'),
    path('remove_single_item_from_cart/<slug>/', remove_single_item_from_cart, name='remove_single_item_from_cart'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    ]