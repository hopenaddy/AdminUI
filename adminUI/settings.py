"""
Django settings for adminUI project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+)ze3x_6sds7%vava^g=+xkwrunoh6(%+!dwljb!l(jb4!3np+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'my_app',
    'loginsys',
    'bootstrapform'
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

ROOT_URLCONF = 'adminUI.urls'

WSGI_APPLICATION = 'adminUI.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
     'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': "yaps",
        'HOST':"127.0.0.1",
        'USER':"root",
        'PASSWORD':"",
        'TEST_MIRROR': 'default'
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        # 'TEST_MIRROR': 'default'
    },
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'Europe/Kiev'

TIME_ZONE = 'Europe/Kiev'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

LOGIN_URL = '/auth/login/'

LOGGING  =  { 
    'version' :  1 , 
    'disable_existing_loggers' :  True ,
    'formatters':{
        'standard':{
            'format':'%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
    }, 
    'handlers' :  { 
        'default' :  { 
            'level' :  'DEBUG' , 
            'class' :  'logging.handlers.RotatingFileHandler' , 
            'filename' :  '/opt/lv128/log/admin_all_operation.log' ,
            'formatter' : 'standard',

        },
         'request_handler' :  { 
            'level' :  'WARNING' , 
            'class' :  'logging.FileHandler' , 
            'filename' :  '/opt/lv128/log/admin_debug.log' ,
            'formatter' : 'standard',
        }, 
    }, 
    'loggers':  { 
        '':{
            'handlers' :  [ 'default' ], 
            'level' :  'DEBUG' , 
            'propagate' :  False ,
        },    
        'django.request':  { 
            'handlers' :  [ 'request_handler' ], 
            'level' :  'DEBUG' , 
            'propagate' :  False , 
        }, 
    }, 
}
