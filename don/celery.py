import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'don.settings')

app = Celery('don')
app.config_from_object('django.conf:settings', namespace = 'CELERY')

app.conf.beat_schedule = {
    'print_every_5_seconds': {
        'task': 'balon.tasks.printer',
        'schedule': 5,
        'args': (5,),
    },
}

app.autodiscover_tasks()