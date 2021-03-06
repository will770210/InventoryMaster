"""
Django settings for InventoryMaster project.

Generated by 'django-admin startproject' using Django 2.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
import logging
import django.utils.log
import logging.handlers

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '14d1s6$n2dov6z!75rzwzrb&p0g)*zfpew($^sn$n*3fldup#w'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['inventorymaster001.herokuapp.com', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'user',
    'store',
    'product',
    'inventory',
    'widget_tweaks',
    'django_apscheduler',
    'dashboard',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware'
]

ROOT_URLCONF = 'InventoryMaster.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            os.path.join(BASE_DIR, 'templates/layouts'),
            os.path.join(BASE_DIR, 'static')
        ]
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

WSGI_APPLICATION = 'InventoryMaster.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

# PostgreSQL 指令:GRANT ALL PRIVILEGES ON DATABASE myproject TO myprojectuser;

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'inventory_master',
        'USER': 'admin',
        'PASSWORD': '12345678',
        'HOST': 'localhost',
        'PORT': '',
    }
}

if os.getenv('DATABASE_URL') is not None:
    import dj_database_url
    DATABASES['default'] = dj_database_url.config()


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'zh-hant'

TIME_ZONE = 'Asia/Taipei'

USE_I18N = True

USE_L10N = True

USE_TZ = True



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'assets')
STATICFILES_DIRS = (os.path.join('static'), )

SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_COOKIE_AGE = 1800
SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'will770210@gmail.com'
EMAIL_HOST_PASSWORD = 'pqhdccwwdobltzdk'
EMAIL_PORT = 587

# 导入模块
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': True,
#     'formatters': {
#         'standard': {'format': '%(asctime)s [%(threadName)s:%(thread)d] [%(name)s:%(lineno)d] [%(module)s:%(funcName)s] [%(levelname)s]- %(message)s'}
#     },
#     'filters': {
#     },
#     'handlers': {
#         # 'mail_admins': {
#         #     'level': 'ERROR',
#         #     'class': 'django.utils.log.AdminEmailHandler',
#         #     'include_html': True,
#         # },
#         # 'default': {
#         #     'level': 'DEBUG',
#         #     'class': 'logging.handlers.RotatingFileHandler',
#         #     'filename': 'all.log',  # 日志输出文件
#         #     'maxBytes': 1024 * 1024 * 5,  # 文件大小
#         #     'backupCount': 5,  # 备份份数
#         #     'formatter': 'standard',  # 使用哪种formatters日志格式
#         # },
#         # 'error': {
#         #     'level': 'ERROR',
#         #     'class': 'logging.handlers.RotatingFileHandler',
#         #     'filename': '/sourceDns/log/error.log',
#         #     'maxBytes': 1024 * 1024 * 5,
#         #     'backupCount': 5,
#         #     'formatter': 'standard',
#         # },
#         'console': {
#             'level': 'DEBUG',
#             'class': 'logging.StreamHandler',
#             'formatter': 'standard'
#         },
#         # 'request_handler': {
#         #     'level': 'DEBUG',
#         #     'class': 'logging.handlers.RotatingFileHandler',
#         #     'filename': '/sourceDns/log/script.log',
#         #     'maxBytes': 1024 * 1024 * 5,
#         #     'backupCount': 5,
#         #     'formatter': 'standard',
#         # },
#         # 'scprits_handler': {
#         #     'level': 'DEBUG',
#         #     'class': 'logging.handlers.RotatingFileHandler',
#         #     'filename': '/sourceDns/log/script.log',
#         #     'maxBytes': 1024 * 1024 * 5,
#         #     'backupCount': 5,
#         #     'formatter': 'standard',
#         # }
#     },
#     'loggers': {
#         'django': {
#             'handlers': [ 'console'],
#             'level': 'DEBUG',
#             'propagate': False
#         },
#     #     'django.request': {
#     #         'handlers': ['request_handler'],
#     #         'level': 'DEBUG',
#     #         'propagate': False,
#     #     },
#     #     'scripts': {
#     #         'handlers': ['scprits_handler'],
#     #         'level': 'INFO',
#     #         'propagate': False
#     #     },
#     #     'sourceDns.webdns.views': {
#     #         'handlers': ['default', 'error'],
#     #         'level': 'DEBUG',
#     #         'propagate': True
#     #     },
#     #     'sourceDns.webdns.util': {
#     #         'handlers': ['error'],
#     #         'level': 'ERROR',
#     #         'propagate': True
#     #     }
#     }
# }