from celery import shared_task
from django.conf import settings


@shared_task(autoretry_for=(ConnectionError,),
             retry_kwargs={'max_retries': 5})
def send_mail(subject, message):
    raise ConnectionError
    recipient = settings.DEFAULT_FROM_EMAIL
    from django.core.mail import send_mail
    from time import sleep
    sleep(10)
    send_mail(
        subject,
        message,
        recipient,
        [recipient],
        fail_silently=False,
    )
    '''
    1 - 2 sec
    2 - 4 sec
    3 - 8 sec
    4 - 16 sec
    5 - error
    '''
