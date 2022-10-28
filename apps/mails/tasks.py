import time

from django_celery_test.celery_mail import app


@app.task
def send_mail():
    """
    mail을 보낸다
    """
    print(f"메일을 보냅니다")
    time.sleep(10)
