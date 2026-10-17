import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "aplx_ams_django.settings.production")

application = get_wsgi_application()
