import time

from apps.posts.models import Post
from django_celery_test.celery_sqs import app
from utils.redis_client import get_redis_client


@app.task(bind=True, acks_late=True, autoretry_for=(ZeroDivisionError,), default_retry_delay=10, max_retries=2)
def send_post_created_alert_sqs(self, post_id: int):
    """
    post 생성 알림을 보낸다
    1. 메시지 유실에 대한 방어처리, worker에서 메시지를 가져온 후 정말 완료 처리 되었다고 오토 커밋
    2. 비즈니스 로직 에러에 대한 예외처리 (익셉션을 감싸서 슬랙 알림 혹은 다른방식으로든 처리하기)
    """

    client = get_redis_client()
    key = self.request.id
    time.sleep(5)
    redis_lock = client.lock(key, timeout=3)
    if redis_lock.acquire(blocking=False):
        post = Post.objects.create(content="잘 되냐?")
        # ZeroDivisionError 를 일으켜 retry 를 확인한다
        a = 1/0
        print(post)
        print(f"{post_id}번 포스트가 생성되었습니다.")
    else:
        print("LOCK IN USE")


@app.task(acks_late=True)
def send_post_read_alert_sqs(post_id: int):
    """
    누가 내 post를 읽었을 때마다 알림을 보낸다
    """
    print(f"{post_id}번 포스트를 누가 읽었습니다.")
