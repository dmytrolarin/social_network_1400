from django.urls import path
from .views import render_registration, render_login, render_welcome


urlpatterns = [
    path('registration/', render_registration, name = "registration"),
    path('login/', render_login, name = "login"),
    path("welcome/", render_welcome, name = "welcome")
]