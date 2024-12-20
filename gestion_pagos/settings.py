# GESTION_PAGOS SETTINGS.PY
from pathlib import Path
from django.utils.translation import gettext_lazy as _
import warnings

# Esta línea debe ser eliminada o comentada
# from django.utils.deprecation import RemovedInDjango50Warning

# Ignorar advertencias relacionadas con la eliminación en Django 5.0
# warnings.filterwarnings("ignore", category=RemovedInDjango50Warning)

import os


# settings.py
DATA_UPLOAD_MAX_NUMBER_FIELDS = 10000  # O un valor mayor dependiendo de tus necesidades

# Configuración de mensajes
from django.contrib.messages import constants as messages

MESSAGE_TAGS = {
    messages.DEBUG: 'debug',
    messages.INFO: 'info',
    messages.SUCCESS: 'success',
    messages.WARNING: 'warning',
    messages.ERROR: 'danger',
}


# Base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent
RECAPTCHA_TEST_MODE = True


# Quick-start development settings - unsuitable for production
SECRET_KEY = 'django-insecure-l!w*xa#rk(9lrdfx3ph6j)x1r_9!%mp+hh-083-tw00caupanr'
DEBUG = False
ALLOWED_HOSTS = ['46.202.151.235', 'localhost', '127.0.0.1']

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'pagos',
    'rest_framework',
    'django_filters',
    'import_export',
    'widget_tweaks',
]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'gestion_pagos.urls'

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
        },
    },
]

WSGI_APPLICATION = 'gestion_pagos.wsgi.application'

# Database configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'telefonica',
        'USER': 'nahum',
        'PASSWORD': 'nahum2020',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}




# Password validation
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
LANGUAGE_CODE = 'es'

TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Custom user model
AUTH_USER_MODEL = 'pagos.CustomUser'

# Logging configuration
# settings.py

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'ERROR',  # Solo mostrar errores del framework Django
            'propagate': True,
        },
        'pagos': {  # Ajustar el logging solo para tu app
            'handlers': ['console'],
            'level': 'DEBUG',  # Muestra depuración solo en esta app
            'propagate': False,
        },
    },
}


LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'menu'

