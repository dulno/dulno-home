import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '***REMOVED***'

MY_SECRET = '***REMOVED***'

# Whether the project should be configured in production, staging or local mode
# Possible values: PRODUCTION, STAGING, LOCAL
ENVIRONMENT = os.getenv('DULNO_ENVIRONMENT', 'LOCAL')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = ENVIRONMENT == 'STAGING' or ENVIRONMENT == 'LOCAL'

if ENVIRONMENT == 'PRODUCTION':
  ALLOWED_HOSTS = ['dulno.com', 'www.dulno.com', '0.0.0.0']
elif ENVIRONMENT == 'STAGING':
  ALLOWED_HOSTS = ['10.96.0.15', '0.0.0.0']
elif ENVIRONMENT == 'LOCAL':
  ALLOWED_HOSTS = ['127.0.0.1', '0.0.0.0']

SECURE_CROSS_ORIGIN_OPENER_POLICY = None

if ENVIRONMENT == 'PRODUCTION':
  COOKIE_DOMAIN = '.dulno.com'
elif ENVIRONMENT == 'STAGING':
  COOKIE_DOMAIN = '.dulno.dev'
elif ENVIRONMENT == 'LOCAL':
  COOKIE_DOMAIN = '127.0.0.1'

BACKEND_ENDPOINT = 'http://10.96.0.4'

# Application definition

INSTALLED_APPS = [
  'base.apps.BaseConfig',
  'errors.apps.ErrorsConfig',
  'home.apps.HomeConfig',
  'django.contrib.admin',
  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.sessions',
  'django.contrib.messages',
  'django.contrib.staticfiles',
  'corsheaders',
]

MIDDLEWARE = [
  'django.middleware.security.SecurityMiddleware',
  'django.contrib.sessions.middleware.SessionMiddleware',
  'django.middleware.locale.LocaleMiddleware',
  'django.middleware.common.CommonMiddleware',
  'django.middleware.csrf.CsrfViewMiddleware',
  'django.contrib.auth.middleware.AuthenticationMiddleware',
  'django.contrib.messages.middleware.MessageMiddleware',
  'django.middleware.clickjacking.XFrameOptionsMiddleware',
  'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'app.urls'

TEMPLATES = [
  {
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [BASE_DIR + "/templates/"],
    'APP_DIRS': True,
    'OPTIONS': {
      'context_processors': [
        'django.template.context_processors.debug',
        'django.template.context_processors.request',
        'django.contrib.auth.context_processors.auth',
        'django.contrib.messages.context_processors.messages',
        'base.context_processors.domain'
      ],
    },
  },
]

WSGI_APPLICATION = 'app.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [
  BASE_DIR + '/static/',
]

LOCALE_PATHS = (
   BASE_DIR + '/locale/',
)

LANGUAGES = (
  ('en', 'English'),
  ('de', 'Deutsch'),
)

WHITELIST = False

LOGGING = {
  'version': 1,
  'disable_existing_loggers': False,
  'handlers': {
    'console': {
      'level': 'DEBUG',
      'class': 'logging.StreamHandler',
    },
    'custom_handler': {
      'level': 'ERROR',
      'class': 'errors.exception.ExceptionHandler',
    },
  },
  'loggers': {
    'django': {
      'handlers': ['console', 'custom_handler'],
      'level': 'DEBUG',
      'propagate': True,
    },
  },
}