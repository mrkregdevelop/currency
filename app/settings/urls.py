from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from currency.views import ProfileView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('auth/', include('django.contrib.auth.urls')),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('account/', include('account.urls')),

    path('__debug__/', include('debug_toolbar.urls')),

    path('', TemplateView.as_view(template_name='index.html'), name='index'),

    path('currency/', include('currency.urls')),
]
