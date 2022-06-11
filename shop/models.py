from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.urls import reverse

CATEGORY_CHOICES = ( # выбор категории
    ('COU', 'Course'),
    ('AL', 'Album'),
    ('CON', 'Consulting')
)

LABEL_CHOICES = ( # выбор популярности
    ('S', 'success'),
    ('P', 'primary'),
    ('W', 'warning')
)

class Item(models.Model):  # модель для товара
    title = models.CharField(max_length=100)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=3)
    label = models.CharField(choices=LABEL_CHOICES, max_length=1)
    slug = models.SlugField()
    description = models.TextField()


    def __str__(self):
        return self.title

    def save(self, *args, **kwargs): # для автоматического добавления слага из тайтла и исполнителя, из формы убрать
        self.slug = slugify(self.title + self.category)
        super(Item, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('ItemDetail', kwargs={'slug': self.slug})

    def get_add_to_cart_url(self): # будет использоваться при нажатии на кнопку добавить в корзину
        return reverse("add_to_cart", kwargs={
            'slug': self.slug
        })

    def get_remove_from_cart_url(self): # будет использоваться при нажатии на кнопку удалить из корзины
        return reverse("remove_from_cart", kwargs={
            'slug': self.slug
        })


class OrderItem(models.Model): # модель для заказанного товара
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)


class Order(models.Model):  # модель корзины
    user = models.ForeignKey(settings.AUTH_USER_MODEL, # для показа корзины под определенного юзера
                             on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    ordered = models.BooleanField(default=False)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()

    def __str__(self):
        return self.user.username
