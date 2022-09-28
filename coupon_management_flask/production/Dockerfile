FROM python:3.9-slim as base

ENV PYTHONFAULTHANDLER=1 \
    PYTHONHASHSEED=random \
    PYTHONUNBUFFERED=1

WORKDIR /app
COPY .. /app/

RUN pip install -r /app/requirements.txt
