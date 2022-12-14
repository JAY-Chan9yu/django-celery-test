import os
import time

import django

os.environ.setdefault("BOTO_DISABLE_COMMONNAME", "true")  # https://github.com/boto/botocore/issues/2705

# Todo: 장고 모듈 사용을 위해 필수
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from apps.posts.tasks import send_post_read_alert, send_post_created_alert
from apps.mails.tasks import send_mail


for i in range(0, 10):
    send_mail.delay()
    send_post_read_alert.delay(i)
    send_post_created_alert.delay(i)
    time.sleep(0.5)
