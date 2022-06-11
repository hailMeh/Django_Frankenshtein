from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.views.generic import ListView, DetailView
from django.utils import timezone
from django.contrib import messages
# Create your views here.


class ItemList(ListView):
    model = Item
    template_name = 'shop/home-page.html'
    context_object_name = 'items'


def checkout_page(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, 'shop/checkout-page.html', context)


class ItemDetail(DetailView):
    model = Item
    template_name = 'shop/product-page.html'


def add_to_cart(request, slug): # принимаем запрос с нужным обьектом/слагом
    item = get_object_or_404(Item, slug=slug) # Возьмем новый обьект из слага или выведем ошибку
    order_item, created = OrderItem.objects.get_or_create(  # присвоим или создадим для модели OrderItem новый обьект из заданного ранее принимаемого слага
        item=item,
        user = request.user,
        ordered = False
        ) # присвоим или создадим для модели OrderItem новый обьект из заданного ранее принимаемого слага
    order_qs = Order.objects.filter(user=request.user, ordered=False) # Проверка через фильтр возврата обьектов на невыполненные заказы у авторизованного юзера
    if order_qs: # если условие успешно
        order = order_qs[0] # возврат первого значения из возвращаемого через условие queryset
        # Проверка на количество
        if order.items.filter(item__slug=item.slug).exists(): # если данный обьектов уже существует в корзине
            order_item.quantity += 1 # то прибавляем к полю количества + 1
            order_item.save() # сохраняем
            messages.info(request, "This item quantity was updated.")
            return redirect("ItemDetail", slug=slug)
        else:
            order.items.add(order_item)
            messages.info(request, "This item was added to your cart.")
            return redirect("ItemDetail", slug=slug)

    else:
        ordered_date = timezone.now() # автоматическое добавление времени создания заказа
        order = Order.objects.create( # создадим новый обьект в модели
        user=request.user, # у авторизованного пользователя
        ordered_date=ordered_date) # добавление в базу врмени создания заказа
        order.items.add(order_item) # и добавим обьект переданный выше через слаг
        messages.info(request, "This item was added to your cart.")
        return redirect("ItemDetail", slug=slug) # возвращаемся на страницу продукта черекз слаг


def remove_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug) # принимаем нужный по слагу обьект
    order_qs = Order.objects.filter( # фильтруем в переменную заказы данного юзера
        user=request.user,
        ordered=False
    )
    if order_qs.exists(): # если хотя бы есть один заказ
        order = order_qs[0] # берем элемент
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            order.items.remove(order_item)
            order_item.delete()
            messages.info(request, "This item was removed from your cart.")
            return redirect("ItemDetail", slug=slug)
        else:
            messages.info(request, "This item was not in your cart")
            return redirect("ItemDetail", slug=slug)
    else:
        messages.info(request, "You do not have an active order")
        return redirect("ItemDetail", slug=slug)