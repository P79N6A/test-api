"""
Django settings for api_server project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
RUN_MODE = os.environ.get("RUN_MODE", "DEVELOP")


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'r@n=qu%s0k0bfopr=sw_xj+)f6ygt5k)+(&^f09qot1d64qb#h'




# test
DEVELOP_MODE_MYSQL = {
}

# official
PRODUCT_MODE_MYSQL ={
}

DATABASES = DEVELOP_MODE_MYSQL

if 'DEVELOP' == RUN_MODE:
    DEBUG = True
    TEMPLATE_DEBUG = True
else:
    DEBUG= False
    TEMPLATE_DEBUG = False
    DATABASES =PRODUCT_MODE_MYSQL

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
)

ROOT_URLCONF = 'api_server.urls'

WSGI_APPLICATION = 'api_server.wsgi.application'

BARAD_API_KEY = 'jXYHLPI01sYdQNN634mZ9SUnROZLQxP9'


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'generic': {
            'format': '%(asctime)s [%(process)d] [%(levelname)s] %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
            'class': 'logging.Formatter'
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'formatter': 'generic',
            'class': 'logging.StreamHandler'
        },
        'error_file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'maxBytes': 1024 * 1024 * 10,
            'backupCount': 5,
            'formatter': 'generic',
            'filename': os.path.join(BASE_DIR, 'var', 'log', 'error.log'),
            },
        'access_file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'maxBytes': 1024 * 1024 * 10,
            'backupCount': 5,
            'formatter': 'generic',
            'filename': os.path.join(BASE_DIR, 'var', 'log', 'django-access.log'),
            }
    },
    'loggers': {
        'django.request': {
            'handlers': ['console', 'access_file'],
            'level': 'DEBUG',
            'propagate': True
        },
        '': {
            'handlers': ['console', 'error_file'],
            'level': 'INFO',
            'propagate': False
        }
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'zh-CN'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
