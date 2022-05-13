from django.conf import settings  # images
from django.conf.urls.static import static  # images
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    #  django-admin
    path('admin/', admin.site.urls),
    #  user-management
    path('accounts/', include('allauth.urls')),  # django-allauth auhtorozation
    #  local apps
    path('', include('pages.urls')),
    path('music/', include('music.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # images
