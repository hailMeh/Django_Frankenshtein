from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe


admin.site.site_title = 'my_music'
admin.site.site_header = 'Administrate this!'

class MusicAdmin(admin.ModelAdmin):
    save_on_top = True


    list_display = ('id', 'title', 'author', 'get_html_photo','description','year', 'price', 'slug','is_published', 'category', 'time_create','time_update','draft') # Что отображать
    list_display_links = ('id', 'title', 'category')  # Линкс на поля для перехода
    fields = ('title', 'author', 'slug', 'cover', 'description','year','price', 'is_published', 'category', 'added_by','draft') # при добавлении через админку, какие поля указывать для заполнения
    search_fields = ('title', 'author', 'category') # поиск по полям
    list_editable = ('price', ) # что можно редактировать
    list_filter = ('title', 'author', 'category')  # фильтрация по
    prepopulated_fields = {"slug": ("title", "author")}  # Автоматические преобразование из field в slug

    def get_html_photo(self, object):
        if object.cover:
            return mark_safe(f"<img src='{object.cover.url}' width=50>")
        else:
            return 'No img'



class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Music, MusicAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Rating)
admin.site.register(RatingStar)
admin.site.register(AlbumShots)
admin.site.register(Reviews)
