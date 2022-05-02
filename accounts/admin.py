from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin # импорт стандартной админки,которая будет расширяться
from .forms import CustomUserCreationForm, CustomUserChangeForm # импорт измененных стандартных форм

CustomUser = get_user_model()  # изменение стандартной модели юзера на кастомную


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm  # Новая форма для создания
    form = CustomUserChangeForm  # Новая форма для редактирования
    model = CustomUser  # модель юзера уже с нашими изменениями
    list_display = ['email', 'username',]  # какие поля отображать в админке, добавитть можно сколько угодно,главное чтобы были в модели


admin.site.register(CustomUser, CustomUserAdmin)  # регистрация измененных стандартных настроек юзера и форм