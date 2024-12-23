import os
import environ

env = environ.Env()


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

env.read_env(os.path.join(BASE_DIR, ".env"))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'd8+lpdyupy-+snp_@iwh3bz)a0@2xf&==4x$v&bqw*axn@2c$d'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Custom User Model
AUTH_USER_MODEL = 'accounts.User'

# Application definition

DJANGO_DEFAULT_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
]

THIRD_PARTY_APPS = [
    'rest_framework',
    'rest_framework.authtoken',
    'drf_spectacular',
]

LOCAL_APPS = [
    'accounts.apps.AccountsConfig',
    'charities.apps.CharitiesConfig',
    'about_us.apps.AboutUsConfig',
]

INSTALLED_APPS = DJANGO_DEFAULT_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'charity.urls'

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

WSGI_APPLICATION = 'charity.wsgi.application'

# Database
DATABASES = {
    "default": {
        "ENGINE": env("SQL_ENGINE", default="django.db.backends.sqlite3"),
        "NAME": env("SQL_DATABASE", default=os.path.join(BASE_DIR, "db.sqlite3")),
        "USER": env("SQL_USER", default="user"),
        "PASSWORD": env("SQL_PASSWORD", default="password"),
        "HOST": env("SQL_HOST", default="localhost"),
        "PORT": env("SQL_PORT", default="5432"),
        "CONN_MAX_AGE": 0,
    }
}

# Password validation
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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'

REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
}

CORS_ORIGIN_ALLOW_ALL = True


STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATIC_URL = "/static/"

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

APP_DOMAIN = env("APP_DOMAIN", default="http://localhost:8000")