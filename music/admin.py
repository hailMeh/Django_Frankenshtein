from django.contrib import admin
from .models import Music
# Register your models here.


class MusicAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "price",)


admin.site.register(Music)
