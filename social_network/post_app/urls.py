from django.urls import path
from .views import render_posts

urlpatterns  = [
    path(route="", view=render_posts)
]