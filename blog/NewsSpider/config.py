from __future__ import absolute_import
from datetime import timedelta
from celery.schedules import crontab

# CELERY_TASK_RESULT_EXPIRES=3600
# CELERY_TASK_SERIALIZER='json'
# CELERY_ACCEPT_CONTENT=['json']
# CELERY_RESULT_SERIALIZER='json'

CELERYBEAT_SCHEDULE = {
    'spider': {
        'task': 'main.spider',
        'schedule': timedelta(minutes=30),
        'args':(),
    },
}
#CELERYBEAT_SCHEDULE = {
#    'add-every-2-seconds': {
#        'task': 'proj.agent.add',
#        'schedule': timedelta(seconds=3),
#        'args': (16, 16)
#    },
#}

CELERY_TIMEZONE = 'UTC'