import os
from pathlib import Path

from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv('../infra_bt/.env')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG', 'FALSE').upper() == 'TRUE'

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '127.0.0.1').split(',')

CSRF_TRUSTED_ORIGINS = [
    'https://*.better-together.acceleratorpracticum.ru/', 'https://*.80.87.109.180', 'https://*.127.0.0.1',
    'http://*.better-together.acceleratorpracticum.ru/', 'http://*.80.87.109.180', 'http://*.127.0.0.1',
]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_filters',
    'djoser',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_swagger',
    'taggit',
    'api.apps.ApiConfig',
    'content.apps.ContentConfig',
    'notifications.apps.NotificationsConfig',
    'projects.apps.ProjectsConfig',
    'users.apps.UsersConfig',
    'corsheaders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'rest_framework.middleware.AuthenticationMiddleware',
    # 'rest_framework.middleware.AuthorizationMiddleware',
]

ROOT_URLCONF = 'backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'libraries': {
                'staticfiles': 'django.templatetags.static',
            },
        },
    },
]

WSGI_APPLICATION = 'backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DB', 'volunteers'),
        'USER': os.getenv('POSTGRES_USER', 'volunteers_user'),
        'PASSWORD': os.getenv('POSTGRES_PASSWORD', ''),
        'HOST': os.getenv('DB_HOST', 'localhost'),
        'PORT': os.getenv('DB_PORT', 5432),
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = Path(BASE_DIR, 'collected_static')

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 10,
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend',],
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
}

DJOSER = {
    'LOGIN_FIELD': 'email',
    'HIDE_USERS': False,
    'USER_CREATE_PASSWORD_RETYPE': True,

    'PERMISSIONS': {'activation': ['rest_framework.permissions.IsAdminUser'],
                    'password_reset': ['rest_framework.permissions.AllowAny'],
                    'password_reset_confirm': ['rest_framework.permissions.AllowAny'],
                    'set_password': ['rest_framework.permissions.CurrentUserOrAdmin'],
                    'username_reset': ['rest_framework.permissions.IsAdminUser'],
                    'username_reset_confirm': ['rest_framework.permissions.IsAdminUser'],
                    'set_username': ['rest_framework.permissions.IsAdminUser'],
                    'user_create': ['rest_framework.permissions.IsAdminUser'],
                    'user_delete': ['rest_framework.permissions.IsAdminUser'],
                    'user': ['rest_framework.permissions.IsAdminUser'],
                    'user_list': ['rest_framework.permissions.IsAdminUser'],
                    'token_create': ['rest_framework.permissions.AllowAny'],
                    'token_destroy': ['rest_framework.permissions.IsAuthenticated'], },
}

CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',
    'http://80.87.109.180:3000',
    'http://better-together.acceleratorpracticum.ru',
    'https://better-together.acceleratorpracticum.ru',
]

CORS_ORIGIN_ALLOW_ALL = os.getenv('DEBUG', 'FALSE').upper() == 'TRUE'

AUTH_USER_MODEL = 'users.User'

# Constants
MAX_LENGTH_NAME = 50
MAX_LENGTH_SLUG = 50
MAX_LENGTH_PASSWORD = 20
MAX_LENGTH_EMAIL = 256
MIN_LENGTH_EMAIL = 5

MAX_LEN_CHAR = 250
LEN_PHONE = 12
MAX_LEN_TEXT_IN_ADMIN = 50

MAX_LEN_NAME = 200
LEN_OGRN = 13
MESSAGE_PHONE_REGEX = 'Номер должен начинаться с +7 и содержать {} цифр.'
MESSAGE_EMAIL_VALID = (
    f'"Длина поля от {MIN_LENGTH_EMAIL} до {MAX_LENGTH_EMAIL} символов"'
)

ORGANIZATION = 'Название: {}> ОГРН: {}> Город: {}'
VOLUNTEER = 'Пользователь: {}> Город: {}> Навыки: {}'
PROJECT = 'Название: {}> Организатор: {}> Категория: {}> Город: {}'
PROJECTPARTICIPANTS = 'Проект: {}> Волонтер: {}'

MIN_LEN_TEXT_FEEDBACK = 10
MAX_LEN_TEXT_FEEDBACK = 750
MESSAGE_TEXT_FEEDBACK_VALID = f'Длина поля от {MIN_LEN_TEXT_FEEDBACK} до {MAX_LEN_TEXT_FEEDBACK} символов'

MIN_LEN_NAME_FEEDBACK = 2
MAX_LEN_NAME_FEEDBACK = 40
MESSAGE_NAME_FEEDBACK_VALID = f'Длина поля от {MIN_LEN_NAME_FEEDBACK} до {MAX_LEN_NAME_FEEDBACK} символов'
MESSAGE_NAME_FEEDBACK_CYRILLIC = 'Введите имя кириллицей'

OGRN_ERROR_MESSAGE = 'ОГРН должен состоять из 13 цифр.'

MIN_LEN_TELEGRAM = 5
MAX_LEN_TELEGRAM = 32
TELEGRAM_ERROR_MESSAGE = 'Ник в Telegram должен начинаться с @ и содержать только буквы, цифры и знаки подчеркивания. От {} до {} символов.'

VALUATIONS_ON_PAGE_ABOUT_US = 4
