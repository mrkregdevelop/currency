from django.contrib import admin
from django.urls import path

from currency.views import (
    list_rates, status_code,
    test_template, rates_create,
    request_methods, rates_update,
    rates_delete, rates_details
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('rate/list/', list_rates),
    path('rate/create/', rates_create),
    path('rate/details/<int:pk>/', rates_details),
    path('rate/update/<int:pk>/', rates_update),
    path('rate/delete/<int:pk>/', rates_delete),
    path('status2/', status_code),
    path('template/', test_template),
    path('rm/', request_methods)
]
