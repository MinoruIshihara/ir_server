import environ
import os

BASE_DIR = environ.Path(__file__) - 2
ROOT_DIR = environ.Path(__file__) - 3

api_env = environ.Env()
api_env_file = str(BASE_DIR.path("config/.env"))
api_env.read_env(api_env_file)

DEBUG = api_env("DEBUG", bool)

SECRET_KEY = api_env("SECRET_KEY")
ROOT_URLCONF = "config.urls"

MEDIA_URL = api_env("MEDIA_URL")
MEDIA_ROOT = api_env("MEDIA_ROOT")


db_env = environ.Env()
db_env_file  = str(ROOT_DIR.path("./db/.env"))
db_env.read_env(db_env_file)

POSTGRES_USER = db_env("POSTGRES_USER")
POSTGRES_PASSWORD = db_env("POSTGRES_PASSWORD")


INSTALLED_APPS = [
    "wallpaper",
    "django.contrib.admin",
    "django.contrib.contenttypes",
    "django.contrib.auth",
    "django.contrib.messages",
    #"django.urls",
    #"django.conf.settings",
    #"django.db",
    "rest_framework",
]

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

MIDDLEWARE = [
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "wallpaper",
        "USER": POSTGRES_USER,
        "PASSWORD": POSTGRES_PASSWORD,
        "HOST": "127.0.0.1",
        "PORT": "5432",
    }
}