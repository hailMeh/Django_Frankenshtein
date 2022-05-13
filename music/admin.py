from django.contrib import admin
from .models import Music, Review


class ReviewInLine(admin.TabularInline):
    model = Review


class MusicAdmin(admin.ModelAdmin):
    inlines = [
        ReviewInLine,
    ]
    list_display = ("title", "author", "price",)


admin.site.register(Music, MusicAdmin)

