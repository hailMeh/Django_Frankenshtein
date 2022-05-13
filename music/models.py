from django.db import models
from django.urls import reverse
import uuid


class Music(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200, verbose_name='Title')
    author = models.CharField(max_length=200, verbose_name='Author')
    price = models.DecimalField(max_digits=6, decimal_places=2)  # для цен

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('music_detail', args=[str(self.id)])
