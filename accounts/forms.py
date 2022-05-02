from django.contrib.auth import get_user_model # импорт дефолтных настроек юзера
from django.contrib.auth.forms import UserCreationForm, UserChangeForm # два стандартных класса для расширения


class CustomUserCreationForm(UserCreationForm):  # изменение создания новых форм

    class Meta:
        model = get_user_model()
        fields = ('email', 'username',)


class CustomUserChangeForm(UserChangeForm):  # изменение редактирования созданных форм

    class Meta:
        model = get_user_model()
        fields = ('email', 'username',)