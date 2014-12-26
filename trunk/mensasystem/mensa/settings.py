"""
Django settings for Site project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)


import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = ""
EMAIL_PORT = 587
EMAIL_HOST_PASSWORD = ""
LIST_OF_EMAIL_RECIPIENTS = ""

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/
ADMINS = (
    ('cqshinn', 'cqshinn92@gmail.com'),   # email will be sent to your_email
)

MANAGERS = ADMINS
SITE_ID = 1


# CACHE_BACKEND = 'db://django_cache'
# CACHE_MIDDLEWARE_SECONDS = 10
# CACHE_MIDDLEWARE_KEY_PREFIX = 10
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '$g7xlsk6n&kev&&#5_ck-j=i6-)%sltxl*s+^6t&klfepwwhd&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# DEBUG = False
TEMPLATE_DEBUG = DEBUG
ALLOWED_HOSTS = ['localhost',]
# ALLOWED_HOSTS = []
# ALLOWED_HOSTS = ['localhost',]
# Application definition

INSTALLED_APPS = (
    'apps.admins.bootstrap3',
    'apps.admins',
    # 'django.contrib.admin.apps.SimpleAdminConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'django.contrib.sites',
    'apps.mensa_app',
    'apps.timesheet',
    'apps.system',
    'apps.message',
    'cronjobs',
)


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'django.middleware.cache.UpdateCacheMiddleware',
    # 'django.middleware.cache.FetchFromCacheMiddleware',
    # 'django.contrib.auth.middleware.RemoteUserMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.request",
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
   # 'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# MIDDLEWARE_CLASSES = [
#
#     'mensa_app.middleware.AutoLogout',
# ]

SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_COOKIE_AGE = 60*5
# AUTO_LOGOUT_DELAY = .5
# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
# MEDIA_ROOT = '/path/to/mydjangosite/media/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
# MEDIA_URL = 'http://www.mydjangosite.com/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
# STATIC_ROOT = "/home/enixdark/mensa/New/mensasystem/static/"
# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
# STATIC_URL = os.path.join(BASE_DIR, "static")
# AUTHENTICATION_BACKENDS = (
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.auth.backends.RemoteUserBackend',
# )
ROOT_URLCONF = 'mensa.urls'

WSGI_APPLICATION = 'mensa.wsgi.application'

from django.contrib import messages

MESSAGE_TAGS = {
            messages.SUCCESS: 'alert-success success',
            messages.WARNING: 'alert-warning warning',
            messages.ERROR: 'alert-danger error'
}

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'Site',
#         'USER': '',
#         'PASSWORD': '',
#         'HOST': '',
#         'PORT': '3306',
#         #'unix_socket': '/opt/lampp/var/mysql/mysql.sock',
#     }
# }


# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Bangkok'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR,  'templates'),
    os.path.join(BASE_DIR,  'admins/bootstrap3/templates'),
    os.path.join(BASE_DIR,  'timesheet/templates'),
)

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        },
    },
    'formatters': {
        'simple': {
            'format': '%(levelname)s %(message)s'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django_crontab': {
            'handlers': ['console'],
            'level': 'INFO',
        }
    }
}

# ALLOW_PARALLEL_RUNS = True
# # CRON_CACHE = 'cron_cache'
#
CRON_CLASSES = [
    "apps.mensa_app.cron.MyCronJob",
    # ...
]

# CRONJOBS = [
#
#     ('*/1 * * * *', 'mensasytem.mensa_app.cron.my_scheduled_job', '> /tmp/last_scheduled_job.log'),
#
# ]