from django.urls import path
from .views import *

urlpatterns = [
    path('', ItemList.as_view(), name='ItemList'),
    path('product/<slug:slug>/', ItemDetail.as_view(), name='ItemDetail'),
    path('add_to_cart/<slug>/', add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<slug>/', remove_from_cart, name='remove_from_cart'),
    path('remove_single_item_from_cart/<slug>/', remove_single_item_from_cart, name='remove_single_item_from_cart'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
    path('request-refund/', RequestRefundView.as_view(), name='request-refund'),
    path('add-coupon/', AddCouponView.as_view(), name='add-coupon')
    ]