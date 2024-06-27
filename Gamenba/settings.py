"""
Django settings for Gamenba project.

Generated by 'django-admin startproject' using Django 5.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from datetime import timedelta
from pathlib import Path

import cloudinary
import cloudinary.uploader
import cloudinary.api



# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-lx!+)tbwfyf02n&5ixc$f5p&g9!arsk$&gv%2zj#)o9qfy-!wr'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


ALLOWED_HOSTS = ['taller-mecanico3-sl66.vercel.app', 'localhost', '127.0.0.1']






# Application definition

INSTALLED_APPS = [
    'admin_interface',
    'colorfield',
    'admin_confirm',
    'multi_captcha_admin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
    'crispy_forms',
    'crispy_bootstrap4',
    'rest_framework',
    'axes', #DEFENDER DEL LOGIN
    'captcha',
    'django_recaptcha',
    'cloudinary',
    
    
]
#CONFIG MULTI CAPTCHA ADMIN
MULTI_CAPTCHA_ADMIN = {
    'engine': 'simple-captcha',
}
CRISPY_TEMPLATE_PACK ='bootstrap4'
X_FRAME_OPTIONS ="SAMEORIGIN"

RECAPTCHA_PUBLIC_KEY = '6Ld_UgIqAAAAACj8ajPXESVfWuB1me8auvYWFW1W'
RECAPTCHA_PRIVATE_KEY = '6Ld_UgIqAAAAAFlijI6H19strBnQ0H6PhgS_rHR2'


#CONFIG AXES
AUTHENTICATION_BACKENDS = [
    
    'axes.backends.AxesStandaloneBackend',

    'django.contrib.auth.backends.ModelBackend',
]


X_FRAME_OPTIONS = "SAMEORIGIN"

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'axes.middleware.AxesMiddleware', #AXES
    
    
]

#CONFIG AXES
AXES_FAILURE_LIMIT = 3  #NUMERO DE INTENTOS FALLIDOS
AXES_COOLOFF_TIME = timedelta(minutes=1)
AXES_LOCKOUT_URL = '/account_locked/'
AXES_RESET_ON_SUCCES = True #REESTABLECE EL CONTADOR CUANDO SE LOGEA 

ROOT_URLCONF = 'Gamenba.urls'

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

WSGI_APPLICATION = 'Gamenba.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases
"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
"""
DATABASES = {
    'default': {
        'ENGINE':   'django.db.backends.postgresql_psycopg2',
        'HOST':     'aws-0-sa-east-1.pooler.supabase.com',
        'NAME':     'postgres',
        'USER':     'postgres.ajynhfztwxbkyeurnadg',
        'PASSWORD': 'taller_mecanico',
        'PORT':     '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'es-cl'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

STATICFILES_DIRS = [BASE_DIR/ 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

#CONFIGURACION DE EMAIL
# settings.py
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False  # Asegúrate de que esta configuración esté correcta
EMAIL_HOST_USER = 'tiniten495@gmail.com'
EMAIL_HOST_PASSWORD = 'ws i o p h x b f n e y a g a l'
DEFAULT_FROM_EMAIL = 'tiniten495@gmail.com'




# pyhton manage.py collectstatic --upload-unhashed-files

# CONFIG de Cloudinary
cloudinary.config(
    cloud_name = 'ddowlkwfk',
    api_key = '136118573985568',
    api_secret = 'BNThEbbK5nK4SAzKc5gek-61CAA'
)

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

#CONFIGURACION PARA LOS MENSAJE
MESSAGE_STORAGE = "django.contrib.messages.storage.cookie.CookieStorage"