from django.db import models
from django.conf import settings


class Item(models.Model):  # модель для товара
    title = models.CharField(max_length=100)
    price = models.FloatField()

    def __str__(self):
        return self.title


class OrderItem(models.Model): # модель для заказанного товара
    item = models.ForeignKey(Item, on_delete=models.CASCADE)


class Order(models.Model):  # модель корзины
    user = models.ForeignKey(settings.AUTH_USER_MODEL, # для показа корзины под определенного юзера
                             on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    ordered = models.BooleanField(default=False)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()

    def __str__(self):
        return self.user.username
