import datetime

from celery import Celery
from django.conf import settings
from kombu import Queue, Exchange

app = Celery(
    "celery-default",
    broker=settings.BROKER_URL,
    include=["apps.posts.tasks"]
)
app.now = datetime.datetime.utcnow

# 여기서 문자열을 사용하는것은 작업자가가 자식 프로세스 직렬화 구성을 하지 않는것을 의미합니다.
# -namespace='CELERY' 의 의미는 셀러리와 관련된 모든 설정은 CELERY_ 라는 prefix로 시작함을 의미
app.config_from_object("django.conf:settings", namespace='CELERY')

# 작업 queue, exchange 생성
app.conf.task_queues = (
    Queue("default", routing_key="task.#"),
    Queue("created_push", Exchange('push'), routing_key="push.created"),
    Queue("read_push", Exchange('push'), routing_key="push.read"),
)

# https://docs.celeryq.dev/en/stable/userguide/routing.html#manual-routing
app.conf.task_default_exchange = 'tasks'
app.conf.task_default_exchange_type = 'topic'
app.conf.task_default_routing_key = 'task.default'

