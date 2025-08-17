import os
from celery import Celery
from celery.schedules import crontab

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

app.conf.beat_schedule = {
    'action_every_monday_8am': {
        'task': 'action',
        'schedule': crontab(0, 0, day_of_month='2-30/2'), #  Выполнять каждый чётный день
        'args': (agrs),
    },
}

app.autodiscover_tasks()