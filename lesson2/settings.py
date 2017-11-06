"""
Django settings for lesson2 project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'f=*7u4@=kje5vvvj8j8scoi9-nrf-yaq0)(nb(qyrsg45_p7h+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
    'art1',
    'app2',
    'mytest',
    'favorite',
    'home',
    'app3_filters',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'lesson2.urls'

WSGI_APPLICATION = 'lesson2.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

TEMPLATE_DIRS = (
    'C:/Users/Сергiй/Desktop/Python_lessons/lesson2/templates',
    'C:/Users/Сергiй/Desktop/Python_lessons/lesson2/app2/templates',
    'C:/Users/Сергiй/Desktop/Python_lessons/lesson2/favorite/templates',
    'C:/Users/Сергiй/Desktop/Python_lessons/lesson2/home/templates',
    'C:/Users/Сергiй/Desktop/Python_lessons/lesson2/app3_filters/templates',
)
STATIC_ROOT = os.path.join(os.path.expanduser('~'), 'C:/Users/Сергiй/Desktop/Python_lessons/lesson2/static/')

TEMPLATE_CONTEXT_PROCESSORS = (
                'django.contrib.auth.context_processors.auth',
                'django.core.context_processors.debug',
                'django.core.context_processors.i18n',
                'django.core.context_processors.media',
                'django.core.context_processors.static',
                'django.core.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                'context_proc.my_ip',)

MEDIA_URL= 'http://127.0.0.1:8000/'
MEDIA_ROOT = 'C:/Users/Сергiй/Desktop/Python_lessons/lesson2/media/'
