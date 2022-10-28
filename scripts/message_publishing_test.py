import time

from apps.posts.tasks import send_post_read_alert, send_post_created_alert
from apps.mails.tasks import send_mail


for i in range(0, 10):
    send_mail.delay()
    send_post_read_alert.delay(i)
    send_post_created_alert.delay(i)
    time.sleep(0.5)
