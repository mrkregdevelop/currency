from decimal import Decimal

from celery import shared_task
from django.conf import settings
from currency.choices import RateCurrencyChoices
import requests

from currency.constants import PRIVATBANK_CODE_NAME
from currency.utils import to_2_places_decimal


@shared_task
def parse_privatbank():
    from currency.models import Rate, Source

    # source = Source.objects.filter(code_name=PRIVATBANK_CODE_NAME).first()
    #
    # if source is None:
    #     source = Source.objects.create(code_name=PRIVATBANK_CODE_NAME, name='PrivatBank')

    source, _ = Source.objects.get_or_create(
        code_name=PRIVATBANK_CODE_NAME,
        defaults={
            'name': 'PrivatBank',
        }
    )

    url = 'https://api.privatbank.ua/p24api/pubinfo?exchange&json&coursid=11'
    response = requests.get(url)
    response.raise_for_status()
    rates = response.json()

    available_currency = {
        'USD': RateCurrencyChoices.USD,
        'EUR': RateCurrencyChoices.EUR,
    }

    for rate in rates:
        if rate['ccy'] not in available_currency:
            continue

        buy = to_2_places_decimal(rate['buy'])
        sale = to_2_places_decimal(rate['sale'])
        currency = rate['ccy']

        last_rate = Rate.objects.filter(
            currency=available_currency[currency],
            source=source
        ) \
            .order_by('-created') \
            .first()

        if last_rate.buy != buy or last_rate.sale != sale:
            Rate.objects.create(
                buy=buy,
                sale=sale,
                currency=available_currency[currency],
                source=source
            )


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
