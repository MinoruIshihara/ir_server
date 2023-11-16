FROM ubuntu:20.04

COPY ./requirements.txt /usr/local/etc

WORKDIR /usr/local/etc
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y libgl1-mesa-dev
RUN apt install -y python3-pip
RUN pip install -r requirements.txt
