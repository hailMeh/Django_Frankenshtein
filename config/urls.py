from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    #  django-admin
    path('admin/', admin.site.urls),
    #  user-management
    path('accounts/', include('django.contrib.auth.urls')),  # джанговская авторизация
    #  local apps
    path('accounts/', include('accounts.urls')),  # для регистрации новых пользователей
    path('', include('pages.urls'))
]
