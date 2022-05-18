from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe


admin.site.site_title = 'my_music'
admin.site.site_header = 'Administrate this!'

class ReviewInLine(admin.TabularInline):
    model = Review


class MusicAdmin(admin.ModelAdmin):
    save_on_top = True


    list_display = ('id', 'title', 'author', 'get_html_photo', 'price', 'slug') # Что отображать
    list_display_links = ('id', 'title')  # Линкс на поля для перехода
    fields = ('title', 'slug', 'cover')
    search_fields = ('title', 'author') # поиск по полям
    list_editable = ('price',) # что можно редактировать
    list_filter = ('title', 'author')  # фильтрация по
    prepopulated_fields = {"slug": ("title",)}  # Автоматические преобразование из field в slug

    def get_html_photo(self, object):
        if object.cover:
            return mark_safe(f"<img src='{object.cover.url}' width=50>")
        else:
            return 'No img'
    inlines = [
        ReviewInLine,
    ]


admin.site.register(Music, MusicAdmin)
