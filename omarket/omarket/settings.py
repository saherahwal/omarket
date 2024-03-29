"""
Django settings for omarket project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '33hqrik=((ldf_6!+z$7dh2@y-1ldo!us*uhtamp^rsy6*2f)i'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'omarket',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'registration',
    'address',
    'business',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'omarket.urls'

WSGI_APPLICATION = 'omarket.wsgi.application'


# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

##DATABASES = {
##    'default': {
##        'ENGINE': 'django.db.backends.sqlite3',
##        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
##    }
##}

DB_NAME = 'omarket'
DB_USER = 'root'
DB_HOST = '127.0.0.1'
DB_PORT = '3306'
DB_PASS = 'svn123123'



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': DB_NAME,
        'USER': DB_USER,             # Not used with sqlite3.
        'PASSWORD': DB_PASS,         # Not used with sqlite3.
        'HOST': DB_HOST,             # Set to empty string for localhost. Not used with sqlite3.
        'PORT': DB_PORT,                
    }
}
# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

STATIC_URL = '/static/'

# template dir definition
TEMPLATE_DIRS = (
       '/templates/',
)

# Media Root - uploaded images
MEDIA_URL = '/uploads/'
MEDIA_ROOT = os.path.join(BASE_DIR, "omarket\uploads")
print "Media_root", MEDIA_ROOT
