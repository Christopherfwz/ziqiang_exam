from __future__ import absolute_import
from datetime import timedelta
from celery.schedules import crontab


CELERYBEAT_SCHEDULE = {
    'spider': {
        'task': 'main.spider',
        'schedule': timedelta(minutes=1),
        'args':(),
    },
}


CELERY_TIMEZONE = 'UTC'