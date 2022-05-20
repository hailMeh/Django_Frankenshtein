from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
import uuid
from django.utils.text import slugify


class Music(models.Model):
    #id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index = True)
    title = models.CharField(max_length=200, verbose_name='Title', db_index = True)
    author = models.CharField(max_length=200, verbose_name='Author')
    description = models.TextField("Описание")
    year = models.PositiveSmallIntegerField("Дата выхода", default=2019)
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
    added_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,
                               verbose_name='Добавил на сайт') # - Передается авторизованный пользователь
    draft = models.BooleanField("Черновик", default=False)

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

    def save(self, *args, **kwargs): # для автоматического добавления слага из тайтла и исполнителя, из формы убрать
        self.slug = slugify(self.title + self.author)
        super(Music, self).save(*args, **kwargs)


class Reviews(models.Model):
    """Отзывы"""
    email = models.EmailField()
    name = models.CharField("Имя", max_length=100)
    text = models.TextField("Сообщение", max_length=5000)
    parent = models.ForeignKey(
        'self', verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True
    )
    music = models.ForeignKey(Music, verbose_name="альбом", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.music}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"


class Category(models.Model):
    name = models.CharField("Категория", max_length=150, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
            return self.name


    def get_absolute_url(self):
            return reverse('category', kwargs={'slug': self.slug})


    class Meta:
            verbose_name = 'Категории'
            verbose_name_plural = 'Категории'


class AlbumShots(models.Model):
    """Постеры из альбома"""
    title = models.CharField("Заголовок", max_length=100)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to="album_shots/")
    album = models.ForeignKey(Music, verbose_name="Альбом", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
            verbose_name = "Постеры из альбома"
            verbose_name_plural = "Постеры из альбома"


class RatingStar(models.Model):
    """Звезда рейтинга"""
    value = models.SmallIntegerField("Значение", default=0)

    def __str__(self):
        return f'{self.value}'

    class Meta:
        verbose_name = "Звезда рейтинга"
        verbose_name_plural = "Звезды рейтинга"
        ordering = ["-value"]


class Rating(models.Model):
    """Рейтинг"""
    ip = models.CharField("IP адрес", max_length=15)
    star = models.ForeignKey('RatingStar', on_delete=models.CASCADE, verbose_name="звезда")
    movie = models.ForeignKey('Music', on_delete=models.CASCADE, verbose_name="альбом", related_name="ratings")

    def __str__(self):
        return f"{self.star} - {self.movie}"

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"
