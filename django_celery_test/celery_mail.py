import datetime

from celery import Celery
from django.conf import settings

app = Celery(
    "celery-mail",
    broker=settings.BROKER_MAIL_URL,
    include=["apps.mails.tasks"]
)

app.now = datetime.datetime.utcnow
app.config_from_object("django.conf:settings", namespace='CELERY-MAIL')

# app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
app.conf.update(
    broker_pool_limit=None,  # connection pool에서 열 수 있는 최대 connection수입니다. None으로 설정하면 connection pool이 비활성화되고 connection이 설정되고 사용할 때마다 닫힙니다.
    # result_expires=3600,  # backend에 데이터가 남아있는 기간을 설정
    task_acks_late=True,  # 기본적으로 작업을 수행하면 작업이 실행되기 직전에 "acked" 되지만 오랜시간이 걸리는 딥러닝 작업의 경우 계산 된 후에만 "acked" 되기 위한 설정
    acks_late=True,
    worker_concurrency=1,  # worker 개수 설정
    worker_prefetch_multiplier=1,  # worker가 받을 메세지 수량을 결정한다. 1로 설정하여 한번에 하나의 메시지만 받도록 설정 (default=4)
    task_serializer="json",
    result_serializer="json",
    accept_content=["json"],
    # prometheus로 모니터링을 하기 위한 설정
    worker_send_task_events=True,
    task_send_sent_event=True,
)
