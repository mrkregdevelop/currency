from django.contrib import admin
from django.urls import path

from currency.views import list_rates, status_code, test_template


urlpatterns = [
    path('admin/', admin.site.urls),
    path('rate/list/', list_rates),
    path('status2/', status_code),
    path('template/', test_template),
]
