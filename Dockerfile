FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY Pipfile Pipfile.lock ./


RUN pip install --upgrade pip
RUN pip install pipenv==v2024.4.0 && pipenv install --system --deploy

COPY . /app/