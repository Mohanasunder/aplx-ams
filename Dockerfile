FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ src/

ENV DJANGO_SETTINGS_MODULE=aplx_ams_django.settings.base
ENV PYTHONPATH=/app/src

CMD ["gunicorn", "aplx_ams_django.wsgi:application", "--bind", "0.0.0.0:8000"]
