from django.urls import path, include
from . import views
from rest_framework.authtoken import views as auth_token
from rest_framework import routers

app_name = 'accounts'
urlpatterns = [
    path('register/', views.UserRegister.as_view(), name='register'),
]

