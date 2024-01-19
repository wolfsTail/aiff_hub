from django.contrib import admin
from django.urls import path

from .endpoints import auth_views, views


app_name = 'oauth'


urlpatterns = [
    path('google_login/', auth_views.google_login, name='google_login'),
    path('me/', views.UserViewSet.as_view({'get': 'retrieve', 'put': 'update'}), name='me'),
]
