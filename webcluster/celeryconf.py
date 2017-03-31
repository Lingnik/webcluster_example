import os

from celery import Celery
from django.conf import settings

print("Setting DJANGO_SETTINGS_MODULE")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webcluster.settings")

print("Loading Celery")
app = Celery('webcluster')

CELERY_TIMEZONE = 'UTC'

print("Loading Django settings")
app.config_from_object('django.conf:settings')

print("Discovering tasks")
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
