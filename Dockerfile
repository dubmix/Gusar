FROM python:slim-buster

RUN mkdir /scrapy
COPY . /scrapy

WORKDIR /scrapy

RUN pip install -r /scrapy/requirements.txt
RUN apt-get update && apt-get install -y vim
