import environ

BASE_DIR = environ.Path(__file__) - 1

env = environ.Env()
env_file = str(BASE_DIR.path(".env"))
env.read_env(env_file)

DEBUG = env("DEBUG", bool)
SECRET_KEY = env("SECRET_KEY")

MEDIA_URL = "/media/"
if DEBUG:
    MEDIA_ROOT = BASE_DIR / "media"
else:
    MEDIA_ROOT = f"/var/www/{BASE_DIR.name}/media"