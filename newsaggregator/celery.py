from celery import Celery
from django.conf import settings
import os 

os.environ.setdefault('DJANGO_SETTINGS_MODULE','newsaggregator.settings')

app = Celery('newsaggregator')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

