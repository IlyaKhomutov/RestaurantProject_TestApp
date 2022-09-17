# syntax=docker/dockerfile:1
FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN useradd -ms /bin/bash newuser
USER newuser
WORKDIR /usr/src/dm_rest

COPY ./requirements.txt /usr/requirements.txt
RUN pip install -r /usr/requirements.txt

COPY . /usr/src/dm_rest
