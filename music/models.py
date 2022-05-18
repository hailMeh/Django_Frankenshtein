from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
import uuid


class Music(models.Model):
    #id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index = True)
    title = models.CharField(max_length=200, verbose_name='Title', db_index = True)
    author = models.CharField(max_length=200, verbose_name='Author')
    price = models.DecimalField(max_digits=6, decimal_places=2)  # для цен
    cover = models.ImageField(upload_to='covers/', blank=True)  # images
    time_create = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Время создания', blank=True)  # Позволяет фиксировать текущее время только в момент первого добавления записи в таблицу БД;
    time_update = models.DateTimeField(
        auto_now=True)  # Фиксирует текущее время всякий раз при изменении или добавлении записи в таблицу БД
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)  # Null чтобы не ругалось
    slug = models.SlugField(max_length=255, unique=True, verbose_name="URL")

    class Meta:
        permissions = [
            ('special_status', 'Can check all music'),
        ]
        verbose_name = 'Музыка'
        verbose_name_plural = 'Альбомы'
        ordering = ['time_create', 'title', 'author', 'category']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('music_detail', kwargs={'slug': self.slug})


class Review(models.Model):
    music = models.ForeignKey(
        Music,
        on_delete=models.CASCADE,
        related_name='reviews',
    )
    review = models.CharField(max_length=255)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.review


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
            return self.name

    def get_absolute_url(self):
            return reverse('category', kwargs={'slug': self.slug})

    class Meta:
            verbose_name = 'Категории'
            verbose_name_plural = 'Категории'