"""
Django settings for before project.

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
SECRET_KEY = 'nw7r0%000mww(vugcy9%k(3m0nd8zq8upkc$me#f4tvdoi3rx@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

CRISPY_TEMPLATE_PACK = 'bootstrap3'
# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main',
    'tictactoe',
    'users',
    'crispy_forms',
    'debug_toolbar',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    #'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'before.urls'

WSGI_APPLICATION = 'before.wsgi.application'


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

PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))
STATIC_URL = '/static/'

TEMPLATE_DIRS = ( PROJECT_PATH+'/template/', )
STATICFILES_DIRS = ( PROJECT_PATH+'/static/',)

LOGIN_URL = 'boardgames_login'
LOGOUT_URL = 'boardgames_logout'
LOGIN_REDIRECT_URL = 'users_home'

'''
to enable toolbar only for user to hide debug-toolbar from everyone in production environment

def show_toolbar():
    if not request.is_ajax() and request.user and request.user.username == 'admin'
        return True
    return False

DEBUG_TOOLBAR_CONFIG = ['SHOW_TOOLBAR_CALLABCK':'post.settings.show_toolbar',]
    

'''
