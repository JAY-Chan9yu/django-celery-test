from celery import shared_task


@shared_task(time_limit=1800, soft_time_limit=1800)
def product_crawling_worker():
    print('제품 크롤링')


@shared_task(time_limit=1800, soft_time_limit=1800)
def update_statistics():
    print('통계 업데이트')


@shared_task(time_limit=1800, soft_time_limit=1800)
def check_api():
    print('api check')
