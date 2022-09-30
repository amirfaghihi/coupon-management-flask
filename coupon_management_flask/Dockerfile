FROM python:3.9-slim as base

ENV PYTHONFAULTHANDLER=1 \
    PYTHONHASHSEED=random \
    PYTHONUNBUFFERED=1

WORKDIR /app
RUN export PATH=/app/

COPY ./* /app/

RUN pip install -r /app/requirements.txt

CMD ["gunicorn", "coupon_management_flask.wsgi:app", "-w", "1", "--bind", "0.0.0.0:8000"]
