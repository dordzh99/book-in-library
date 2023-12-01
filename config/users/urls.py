from django.urls import path

from .views import register_user

app_name = 'users'

urlpatterns = [
    path('users/', register_user),
]
