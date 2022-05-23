from django.conf import settings  # images
from django.conf.urls.static import static  # images
from django.contrib import admin
from django.urls import path, include
from music.views import authneed

urlpatterns = [
    #  django-admin
    path('anything-but-admin/', admin.site.urls),
    #  user-management
    path('accounts/', include('allauth.urls')),  # django-allauth auhtorozation
    #  local apps
    path('', include('pages.urls')),
    path('music/', include('music.urls')),
    path('captcha/', include('captcha.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # images

if settings.DEBUG:
    import debug_toolbar # debug-toolbar только в режиме разработки.
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

# Обработчик Хэндлеров, дебюг в false
handler403 = authneed

''' для разворачивания в инете, статика чтобы загружалась. импорт двух библиотек а дальше копипаста в if  
    from django.views.static import serve as mediaserve
from django.conf.urls import url

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

else:
    urlpatterns += [
        url(f'^{settings.MEDIA_URL.lstrip("/")}(?P<path>.*)$',
            mediaserve, {'document_root': settings.MEDIA_ROOT}),
        url(f'^{settings.STATIC_URL.lstrip("/")}(?P<path>.*)$',
            mediaserve, {'document_root': settings.STATIC_ROOT}),
    ]
  '''