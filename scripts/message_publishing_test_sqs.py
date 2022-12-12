import os

import django

os.environ.setdefault("BOTO_DISABLE_COMMONNAME", "true")  # https://github.com/boto/botocore/issues/2705

# Todo: 장고 모듈 사용을 위해 필수
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from apps.posts.sqs_tasks import send_post_created_alert, send_post_read_alert


for i in range(0, 5):
    # send_mail.delay()
    send_post_read_alert.delay(i)
    send_post_created_alert.delay(i)
    # time.sleep(1)z
    print('publishing')


