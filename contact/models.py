from django.db import models
from django.contrib.auth import get_user_model
from django.db import models


class Contact(models.Model):
    """Форма обратной связи по email"""
    added_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,
                                 verbose_name='Отправил')
    email = models.EmailField()
    description = models.TextField("Описание")
    date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Время создания')

    def __str__(self):
        return self.email