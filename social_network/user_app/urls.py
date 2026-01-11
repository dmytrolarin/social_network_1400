from django.urls import path
from .views import render_registration, render_login, render_welcome, logout_view
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('registration/', render_registration, name = "registration"),
    path('login/', render_login, name = "login"),
    path("welcome/", render_welcome, name = "welcome"),
    #path("logout/", LogoutView.as_view(next_page='login'), name='logout')
    path('logout/', logout_view, name= 'logout')
]