from django.urls import path
from .views import render_registration

urlpatterns = [
    path('registration/', render_registration, name = "registration")
]