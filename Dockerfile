FROM python:3.10

COPY ./requirements.txt /usr/local/etc

WORKDIR /usr/local/etc
RUN pip install -r requirements.txt