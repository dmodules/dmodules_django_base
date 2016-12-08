# -*- coding: utf-8 -*-
import os
gettext = lambda s: s
APP_DIR = '/localapp/'

try:
    from settings_local import *
except ImportError:
    pass

ALLOWED_HOSTS = ['localhost', '*',]

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '@lqhi6_f-2nqgn&tck3t_b=+darg9+3172@@x+*3tt%kncrgjt'

TEMPLATE_DEBUG = DEBUG

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'storages',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'urls'


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Montreal'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATICFILES_DIRS = (('/localapp/static/'),)

MEDIA_ROOT = os.path.join('/data/media/')
STATIC_ROOT = os.path.join(APP_DIR, '/data/static_collected/')

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            ### ADD YOUR DIRECTORY HERE LIKE SO:
            APP_DIR + '/templates/',
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.core.context_processors.media',
            ],
        },
    },
]


if DEBUG:

    STATIC_URL = '/static/'
    MEDIA_URL = '/media/'

else:

    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

    AWS_ACCESS_KEY_ID = 'AKIAJVPTTLUUAOR6I3QA'

    AWS_SECRET_ACCESS_KEY = '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'

    AWS_AUTO_CREATE_BUCKET = True

    AWS_HEADERS = {  # see http://developer.yahoo.com/performance/rules.html#expires
        'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
        'Cache-Control': 'max-age=94608000',
    }

    AWS_STORAGE_BUCKET_NAME = 'dmodules_django_base'

    AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

    STATIC_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN
    # MEDIA_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN
    MEDIA_URL = '/media/'



