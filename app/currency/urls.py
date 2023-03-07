from django.urls import path

from currency.views import (
    RateListView,
    RateCreateView,
    RateDetailView,
    RateUpdateView,
    RateDeleteView, ContactUsCreateView
)

app_name = 'currency'


urlpatterns = [
    path('rate/list/', RateListView.as_view(), name='rate-list'),
    path('rate/create/', RateCreateView.as_view(), name='rate-create'),
    path('rate/details/<int:pk>/', RateDetailView.as_view(), name='rate-details'),
    path('rate/update/<int:pk>/', RateUpdateView.as_view(), name='rate-update'),
    path('rate/delete/<int:pk>/', RateDeleteView.as_view(), name='rate-delete'),

    path('contact-us/create/', ContactUsCreateView.as_view(), name='contact-us-create')
]
