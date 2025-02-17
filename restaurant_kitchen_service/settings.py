import os
from pathlib import Path
from dotenv import load_dotenv

import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

SECRET_KEY = 'django-insecure-fy8gn7ui1(2bao!oswa%czjisd&_b5m9lx$%t#=)%@)-2z)9f)'

DEBUG = os.getenv("DEBUG") != "False"

ALLOWED_HOSTS = ["127.0.0.1",
                 "kitchen-mate.onrender.com"]

INTERNAL_IPS = [
    "127.0.0.1",
]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "debug_toolbar",
    "crispy_forms",
    "kitchen",
    "crispy_bootstrap5",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "restaurant_kitchen_service.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
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

CRISPY_TEMPLATE_PACK = "bootstrap5"

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

WSGI_APPLICATION = "restaurant_kitchen_service.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

db_from_env = dj_database_url.config(
    default=os.getenv("DATABASE_URL"),
    conn_max_age=500
)

DATABASES["default"].update(db_from_env)

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation."
        "UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation." 
                "MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation." 
                "CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation." 
                "NumericPasswordValidator",
    },
]

AUTH_USER_MODEL = "kitchen.Cook"

LOGIN_REDIRECT_URL = "/"

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

STATIC_URL = "static/"

STATICFILES_DIRS = (BASE_DIR / "static",)

STATIC_ROOT = BASE_DIR / "staticfiles/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"