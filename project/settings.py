"""
Django settings for project project.

Generated by 'django-admin startproject' using Django 4.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path, os
from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
if os.path.exists(f"{BASE_DIR}/.env"):
    load_dotenv(f"{BASE_DIR}/.env")


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-+8r4y2e9ny@nc^%l-*e%z_o$@1iy5*ot_)o)-74jrig1xna#zq"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("DEBUG")

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    # django apps
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # installed apps
    "rest_framework",
    "django_filters",
    "corsheaders",
    "django_apscheduler",
    # created apps
    "core",
    "report",
    "post",
    "suggestion",
    "notice",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

CORS_ORIGIN_WHITELIST = ["http://127.0.0.1:5173", "http://localhost:5173"]
CORS_ORIGIN_CREDENTIALS = True
CROS_ORIGIN_ALLOW_ALL = True

ROOT_URLCONF = "project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "project.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 10,
    "DEFAULT_FILTER_BACKENDS": ["django_filters.rest_framework.DjangoFilterBackend"],
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "ko-kr"

TIME_ZONE = "Asia/Seoul"

USE_I18N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"

API_URL = os.getenv("API_URL")
WEB_URL = os.getenv("WEB_URL")

DISCORD_WEBHOOK_URL_NEMO = os.getenv("DISCORD_WEBHOOK_URL_NEMO")
DISCORD_WEBHOOK_URL_COMMON = os.getenv("DISCORD_WEBHOOK_URL_COMMON")
DISCORD_WEBHOOK_URL_COMMENT = os.getenv("DISCORD_WEBHOOK_URL_COMMENT")
DISCORD_WEBHOOK_URL_SUGGESTION = os.getenv("DISCORD_WEBHOOK_URL_SUGGESTION")
DISCORD_WEBHOOK_URL_UPLOAD = os.getenv("DISCORD_WEBHOOK_URL_UPLOAD")
DISCORD_WEBHOOK_URL_TEST = os.getenv("DISCORD_WEBHOOK_URL_TEST")


# Apscheduler
APSCHEDULER_DATETIME_FORMAT = "N j, Y, f:s a"  # Default
APSCHEDULER_RUN_NOW_TIMEOUT = 25  # Seconds
