from django.core.validators import FileExtensionValidator
from django.db import models


class Video(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField() # описание
    image = models.ImageField(upload_to='images/') # превью к видео
    file = models.FileField( # загрузка видео-файла
        upload_to='video/',
        validators=[FileExtensionValidator(allowed_extensions=['mp4'])] # валидатор только для mp4 файлов
    )
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title