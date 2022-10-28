from django_celery_test.celery import app


@app.task(queue="created_push", exchange="push")
def send_post_created_alert(post_id: int):
    """
    post 생성 알림을 보낸다
    """
    print(f"{post_id}번 포스트가 생성되었습니다.")


@app.task(queue="read_push", exchange="push")
def send_post_read_alert(post_id: int):
    """
    누가 내 post를 읽었을 때마다 알림을 보낸다
    """
    print(f"{post_id}번 포스트를 누가 읽었습니다.")
