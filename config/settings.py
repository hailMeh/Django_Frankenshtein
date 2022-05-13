from pathlib import Path
from environs import Env

env = Env()
env.read_env()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = env("DJANGO_SECRET_KEY")

DEBUG = env.bool("DJANGO_DEBUG")

ALLOWED_HOSTS = ['community.pythonanywhere.com', 'localhost', '127.0.0.1']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    # local
    'music.apps.MusicConfig',
    'accounts.apps.AccountsConfig',
    'pages.apps.PagesConfig',
    #  3rd-party apps
    'bootstrap5',
    "crispy_forms",
    "crispy_bootstrap5",
    'allauth',
    'allauth.account',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    "default": env.dj_db_url("DATABASE_URL", default="postgres://postgres@db/postgres")
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = [str(BASE_DIR.joinpath('static'))]
STATIC_ROOT = str(BASE_DIR.joinpath('staticfiles'))
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'accounts.CustomUser'  # Дефолтные настройки теперь будут настраиваемы

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"  # ДЛЯ ФОРМ БУТСТРАПА
CRISPY_TEMPLATE_PACK = "bootstrap5"  # ДЛЯ ФОРМ БУТСТРАПА

# django-allauth config
LOGIN_REDIRECT_URL = 'home'
ACCOUNT_LOGOUT_REDIRECT = 'home'
SITE_ID = 1
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'  # автоматически будет отправлять на почту подтверждение при регистрации
EMAIL_HOST = 'smtp.mail.ru'
EMAIL_PORT = '2525'
EMAIL_HOST_USER = 'sultanhabibi@mail.ru'
EMAIL_HOST_PASSWORD = '94Zftb1k2qWT2fN4nhyz'
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# ACCOUNT_SESSION_REMEMBER = True # при выходе пользователя с сайта сохранять ли его сессию?
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = True  # нужно ли при регистрации два раза ввести пароль?
ACCOUNT_USERNAME_REQUIRED = True  # нужно ли при регистрации указывать свой логин?
ACCOUNT_AUTHENTICATION_METHOD = 'email'  # имя пользователя или его логин используются для авторизации
ACCOUNT_EMAIL_REQUIRED = True  # Пользователю необходимо указать e-mail при регистрации
ACCOUNT_UNIQUE_EMAIL = True  # Пользователь только с уникальным емайлом может зарегистрироваться

MEDIA_URL = '/media/'
MEDIA_ROOT = str(BASE_DIR.joinpath('media'))