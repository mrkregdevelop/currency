from django.db import models

from currency.choices import RateCurrencyChoices


class Rate(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    currency = models.PositiveSmallIntegerField(
        choices=RateCurrencyChoices.choices,
        default=RateCurrencyChoices.USD
    )  # if field has choices - get_{field_name}_display(), get_currency_display()
    buy = models.DecimalField(max_digits=6, decimal_places=2)
    sell = models.DecimalField(max_digits=6, decimal_places=2)
    source = models.CharField(max_length=25)

    def __str__(self):
        return f'Currency: {self.get_currency_display()}, Buy: {self.buy}'


class Source(models.Model):
    name = models.CharField(max_length=64)


class ContactUs(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=128)
    email = models.EmailField()
    subject = models.CharField(max_length=256)
    message = models.TextField()


"""
SMTP - Simple mail transfer protocol

User form
name: Taras
email: taras@example.com
subject: Test
body: Test body

Send email to support

recipient: support@example.com
subject: User ContactUs

body: Request from: Taras. Reply to email: taras@example.com. Subject: Test, Body: Test body
"""