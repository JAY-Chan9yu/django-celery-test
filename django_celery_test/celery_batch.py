from __future__ import absolute_import

import datetime
from django.conf import settings
from celery import Celery
from celery.schedules import crontab


app = Celery(
    'celery-batch',
    broker=settings.BROKER_BATCH_URL,
    include=["batches.tasks"]
)

app.now = datetime.datetime.utcnow

app.config_from_object('django.conf:settings')

# worker prefetch 2로 설정
worker_prefetch_multiplier = 2

# https://docs.celeryq.dev/en/stable/userguide/periodic-tasks.html#crontab-schedules
app.conf.beat_schedule = {
    # 제품 크롤링
    'product_crawling_worker': {
        'task': 'batches.tasks.product_crawling_worker',
        'schedule': crontab(minute="*/30"),
        'options': {},
        'args': ()
    },
    # 통계 업데이트
    'update_statistics': {
        'task': 'batches.tasks.update_statistics',
        'schedule': crontab(hour=2, minute=0),
        'options': {},
        'args': ()
    },
    # api check
    'check_api': {
        'task': 'batches.tasks.check_api',
        'schedule': 1,  # 1초마다 실행
        'options': {},
        'args': ()
    },
}
