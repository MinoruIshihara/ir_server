FROM python:3.10

COPY ./wallpaper_api /usr/src/app:delegated

WORKDIR /usr/src/app:delegated/config
RUN pip install -r requirements.txt

WORKDIR /usr/src/app:delegated
CMD gunicorn "--config" "gunicorn_settings.py"