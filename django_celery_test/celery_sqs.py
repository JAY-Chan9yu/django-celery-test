import datetime

from urllib.parse import quote

from celery import Celery
from django.conf import settings

BROKER_URL = f'sqs://{quote(settings.AWS_ACCESS_KEY_ID, safe="")}:{quote(settings.AWS_SECRET_ACCESS_KEY, safe="")}@'

app = Celery(
    "celery-default",
    broker=BROKER_URL,
    include=["apps.posts.sqs_tasks"],
)

app.now = datetime.datetime.utcnow

CELERY_accept_content = ['application/json']
CELERY_task_serializer = 'json'
task_default_queue = 'TestQueue'

BROKER_TRANSPORT_OPTIONS = {
    "region": "ap-northeast-2",
    'polling_interval': 60,
    'visibility_timeout': 10,
}
CELERY_result_backend = None
app.conf.update(broker_transport_options=BROKER_TRANSPORT_OPTIONS)
