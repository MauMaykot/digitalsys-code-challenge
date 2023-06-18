import os

from celery import Celery

from lfg_system.settings import CELERY_TIMEZONE

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lfg_system.settings')

app = Celery('lfg_system')
app.conf.enable_utc = False
app.conf.update(timezone=CELERY_TIMEZONE)

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()