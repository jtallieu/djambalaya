"""
Django settings for webapp project.

Generated by 'django-admin startproject' using Django 1.10.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os, sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'cmvze15krnk8ntcmg(g*10)ikqqbnw6bv_kmca7yr)y+k^g$nc'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'rest_framework',
    'rest_framework_docs',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_filters',
    'django_celery_results',
    'stefani',
]

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_AUTHENTICATION_CLASSES': [],
    'DEFAULT_PERMISSION_CLASSES': [],
}
REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
    #'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 10
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

ROOT_URLCONF = 'webapp.urls'

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

WSGI_APPLICATION = 'webapp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
"""
DB_NAME = os.environ.get('PG_DBNAME', 'stefani')
DB_HOST = os.environ.get('PG_HOST', 'postgres')
DB_USER = os.environ.get('PG_USER', 'webservice')
DB_PASSWORD = os.environ.get('PG_PASSWORD', 'something')
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': DB_NAME,
        'HOST': DB_HOST,
        'USER': DB_USER,
        'PASSWORD': DB_PASSWORD,
    }
}
"""

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
CASSANDRA_FALLBACK_ORDER_BY_PYTHON = True

# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/
STATICFILES_DIRS = [
    '/usr/src/website/src/'
]
STATIC_URL = '/static/'

__LOG_FORMAT = os.environ.get('EEN_LOG_FORMAT', '%(asctime)s.%(msecs).03d[%(levelname)0.3s] %(name)s:%(funcName)s.%(lineno)d %(message)s')
# __LOG_FORMAT = os.environ.get('EEN_LOG_FORMAT', '%(message)s')
__DATE_FORMAT = os.environ.get('EEN_LOG_DATE_FORMAT', '%m-%d %H:%M:%S')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': __LOG_FORMAT,
            'datefmt': __DATE_FORMAT
        },
        'terse': {
            'format': "%(message)s",
            'datefmt': __DATE_FORMAT
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        }
    },
    'handlers': {
        'stdout': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'stream': sys.stdout,
            'formatter': 'verbose'
        },
        'stderr': {
            'level': 'ERROR',
            'class': 'logging.StreamHandler',
            'stream': sys.stderr,
            'formatter': 'verbose'
        },
    },
    'loggers': {
        # Any message not caught by a lower level logger OR
        # Propagates the message to this level will be filtered at
        # the root.
        '': {
            'handlers': ['stdout'],
            'level': os.environ.get('LOGLEVEL_ROOT', 'DEBUG'),
            'propagate': False,
        },
        'webapp': {
            'handlers': ['stdout'],
            'level': os.environ.get('LOGLEVEL_WEBAPP', 'DEBUG'),
            'propagate': False,
        },
        'stefani': {
            'handlers': ['stdout'],
            'level': os.environ.get('LOGLEVEL_STEFANI', 'DEBUG'),
            'propagate': False,
        },
        'stefani.web': {
            'handlers': ['stdout'],
            'level': os.environ.get('LOGLEVEL_WEBAPP', 'DEBUG'),
            'propagate': False,
        },
    }
}