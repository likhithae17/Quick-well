"""
Django settings for QUICK_WELL project.

Generated by 'django-admin startproject' using Django 2.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
from machina import get_apps as get_machina_apps
from machina import MACHINA_MAIN_TEMPLATE_DIR
from machina import MACHINA_MAIN_STATIC_DIR



# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ji$74%!avw55^6h)!r9f@8elxuqavh@-64q=3ufw1#b!26ei-q'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'med.apps.MedConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'docapp.apps.DocappConfig',
    'home.apps.HomeConfig',
<<<<<<< HEAD
    'channels',
    'chat',
    # Machina related apps:
    'mptt',
    'haystack',
    'widget_tweaks',
    'ads',
    'sekizai'

] + get_machina_apps()
=======



]
>>>>>>> 155432cf65498f268a7d3592193b8c77c576d0f5
    #'django_elasticsearch_dsl',



#ELASTICSEARCH_DSL = {
#    'default':{
#        'hosts': 'localhost:9200'
#    }
#}
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'machina.apps.forum_permission.middleware.ForumPermissionMiddleware',
]

ROOT_URLCONF = 'QUICK_WELL.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'machina.core.context_processors.metadata',
                'sekizai.context_processors.sekizai',
            ],
        },
    },
]

WSGI_APPLICATION = 'QUICK_WELL.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'quickwelldb'),
        'TEST': {
            'NAME': os.path.join(BASE_DIR, 'db_test.sqlite3')
        }
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

ASGI_APPLICATION = 'quickwell.routing.application'
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('127.0.0.1', 6379)],
        },
    },
}

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
    MACHINA_MAIN_STATIC_DIR,
]

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    },
    'machina_attachments': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/tmp',
    },
}

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': os.path.join(BASE_DIR, 'whoosh_index'),
    },
}

ADS_GOOGLE_ADSENSE_CLIENT = 'ca-pub-DEFAULT'  # OPTIONAL - DEFAULT TO None

ADS_ZONES = {
    'header': {
        'name': ('Header'),
        'ad_size': {
            'xs': '720x150',
            'sm': '800x90',
            'md': '800x90',
            'lg': '800x90'
        },
        'google_adsense_slot': 'DEFAULT',  # OPTIONAL - DEFAULT TO None
        'google_adsense_format': 'auto',  # OPTIONAL - DEFAULT TO None
    },
    'content': {
        'name': ('Content'),
        'ad_size': {
            'xs': '720x150',
            'sm': '800x90',
            'md': '800x90',
            'lg': '800x90'
        },
        'google_adsense_slot': 'DEFAULT',  # OPTIONAL - DEFAULT TO None
        'google_adsense_format': 'auto',  # OPTIONAL - DEFAULT TO None
    },
    'sidebar': {
        'name': ('Sidebar'),
        'ad_size': {
            'xs': '720x150',
            'sm': '800x90',
            'md': '800x90',
            'lg': '800x90'
        },
        'google_adsense_slot': 'DEFAULT',  # OPTIONAL - DEFAULT TO None
        'google_adsense_format': 'auto',  # OPTIONAL - DEFAULT TO None
    },
}



