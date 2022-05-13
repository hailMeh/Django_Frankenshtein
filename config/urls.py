from django.conf import settings  # images
from django.conf.urls.static import static  # images
from django.contrib import admin
from django.urls import path, include
from music.views import authneed

urlpatterns = [
    #  django-admin
    path('admin/', admin.site.urls),
    #  user-management
    path('accounts/', include('allauth.urls')),  # django-allauth auhtorozation
    #  local apps
    path('', include('pages.urls')),
    path('music/', include('music.urls')),
    path('captcha/', include('captcha.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # images


# Обработчик Хэндлеров, дебюг в false
handler403 = authneed
