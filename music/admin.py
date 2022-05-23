from django.contrib import admin
from django import forms
from .models import *
from django.utils.safestring import mark_safe
from ckeditor_uploader.widgets import CKEditorUploadingWidget


admin.site.site_title = 'my_music'
admin.site.site_header = 'Administrate this!'



class MusicAdminForm(forms.ModelForm):  # ckeditor
    description = forms.CharField(label='Описание',widget=CKEditorUploadingWidget()) # Из модели Music поле для описания обьекта
    class Meta:
        model = Music
        fields = '__all__'


class ReviewInline(admin.TabularInline):
    """Отзывы на странице фильма"""
    model = Reviews
    extra = 1 # дополнительные поля для добавления отзывов из альбома
    readonly_fields = ("name", "email")



class AlbumShotsInline(admin.TabularInline):
    model = AlbumShots
    extra = 1
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f"<img src='{obj.image.url}' width=100>")

    get_image.short_description = "Изображение"

@admin.register(Music)
class MusicAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ('id', 'title', 'author', 'get_html_photo','description','year', 'price', 'slug','is_published', 'category', 'time_create','time_update','draft') # Что отображать
    list_display_links = ('id', 'title', 'category')  # Линкс на поля для перехода
    fields = ('title', 'author', 'slug', 'cover', 'description','year','price', 'is_published', 'category','added_by','draft') # при добавлении через админку, какие поля указывать для заполнения
    search_fields = ('title', 'author', 'category') # поиск по полям
    list_editable = ('price', ) # что можно редактировать
    list_filter = ('title', 'author', 'category')  # фильтрация по
    prepopulated_fields = {"slug": ("title", "author")}  # Автоматические преобразование из field в slug
    inlines = [AlbumShotsInline, ReviewInline]
    form = MusicAdminForm # cdeditor


    def get_html_photo(self, object):
        if object.cover:
            return mark_safe(f"<img src='{object.cover.url}' width=50>")
        else:
            return 'No img'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name') # ссылки для перехода на текущую категорию из списка
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Reviews)
class ReviewAdmin(admin.ModelAdmin):
    """Отзывы к фильму"""
    list_display = ("name", "email", "parent", "music", "id")
    readonly_fields = ("name", "email") # скрытие от редактирования


@admin.register(AlbumSong)
class AlbumSongAdmin(admin.ModelAdmin):
    list_display = ("title", "audio_file", "album")


@admin.register(AlbumShots)
class AlbumShotsAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "get_html_photo", "album")


    def get_html_photo(self, object):  # для вывода миниатюры изображения в админке, указать поле в list_display
        if object.image:
            return mark_safe(f"<img src='{object.image.url}' width=100>")
        else:
            return 'No img'




admin.site.register(Rating)
admin.site.register(RatingStar)


