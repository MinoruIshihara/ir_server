import environ

BASE_DIR = environ.Path(__file__) - 2
ROOT_DIR = environ.Path(__file__) - 3

api_env = environ.Env()
api_env_file = str(BASE_DIR.path("config/.env"))
api_env.read_env(api_env_file)

DEBUG = api_env("DEBUG", bool)

SECRET_KEY = api_env("SECRET_KEY")

POSTGRES_USER = api_env("POSTGRES_USER")
POSTGRES_PASSWORD = api_env("POSTGRES_PASSWORD")

AUTH_USER_MODEL = "wallpaper.User"

ROOT_URLCONF = "config.urls"

MEDIA_URL = "/imagefiles/"
MEDIA_ROOT = f"/var/www/wallpaper_api/images"

STATIC_ROOT = "static"
STATIC_URL = "/static/"

if DEBUG:
    ALLOWED_HOSTS = ["*"]
else:
    ALLOWED_HOSTS = ["127.0.0.1"]

CORS_ALLOW_CREDENTIALS = True
CORS_ALLOWED_ORIGINS = api_env("TRUSTED_ORIGINS").split(" ")
CORS_PREFLIGHT_MAX_AGE = 60 * 30

INSTALLED_APPS = [
    "wallpaper",
    "corsheaders",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "rest_framework.authtoken",
    "rest_framework_nested",
]

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

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
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
        "HOST": "postgres-host",
        "PORT": "5432",
    }
}
