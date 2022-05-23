# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt

RUN apt update && apt install -y build-essential && apt install default-libmysqlclient-dev -y

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 8000

WORKDIR librarymgmt
CMD gunicorn app:app