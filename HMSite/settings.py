"""
Django settings for HMSite project.
For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import sys
try:
    # dateutil is an absolute requirement
    import dateutil
except ImportError:
    raise ImportError('..')

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


TEMPLATE_DIRS = (os.path.join(BASE_DIR, 'templates'),)
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'm@w#p&6p+pt&5bhq+a)@5q_&0xcg#@s-1#xhp0i0js(f69%@y)'

AUTH_USER_MODEL = 'HMS.MyUser'
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

LOGIN_REDIRECT_URL = '/HMS/home'

ALLOWED_HOSTS = []

TEMPLATE_CONTEXT_PROCESSORS =  (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    "swingtime.context_processors.current_datetime",
    "django.core.context_processors.request",
 #   "allauth.account.context_processors.account",
)

LOGIN_URL = 'django.contrib.auth.views.login'

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)
# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
	'HMS',
    'swingtime',
    #'allauth',
    #'allauth.account',
)

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    'HMS/templates',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
 #   "allauth.account.auth_backends.AuthenticationBackend",
)

ROOT_URLCONF = 'HMSite.urls'

WSGI_APPLICATION = 'HMSite.wsgi.application'

#ACCOUNT_AUTHENTICATION_METHOD = "email"
#ACCOUNT_USER_MODEL_USERNAME_FIELD = None
#ACCOUNT_EMAIL_REQUIRED = True
#ACCOUNT_USERNAME_REQUIRED = False
#ACCOUNT_EMAIL_VERIFICATION = "mandatory"
#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

SWINGTIME_SETTINGS_MODULE = 'swingtime.conf.swingtime_settings'

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'Hospmgmtad@gmail.com'
EMAIL_HOST_PASSWORD = 'Hospital'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'Hospmgmtad@gmail.com'

try:
    import django_extensions
except ImportError:
    pass
else:
    INSTALLED_APPS += ('django_extensions',)
    
# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SITE_ID = 1
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
