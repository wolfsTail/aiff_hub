from django.contrib import admin
from django.urls import path

from .endpoints import auth_views, views


app_name = 'oauth'


urlpatterns = [
    path('', auth_views.google_login, name='google_login'),
]
