from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpRequest
from django.db.utils import IntegrityError


def render_registration(request: HttpRequest):
    error = ""
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        password_confirm = request.POST.get("password_confirm")
        if password == password_confirm:
            try:
                User.objects.create_user(username=username, password=password)
                return redirect('login')
            except IntegrityError:
                error = "Такий користовач вже існує"
        else:
            error = "Паролі не співпадають"
    return render(request, 'user_app/registration.html', context={"error": error})


def render_login(request: HttpRequest):
    error = ""
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('welcome')
        else:
            error = "Логін або пароль невірно вказані."
            
    return render(request, 'user_app/login.html', context={"error":error})


def logout_view(request):
    logout(request)
    return redirect('login')


def render_welcome(request: HttpRequest):
    if request.user.is_authenticated: 
        return render(request, 'user_app/welcome.html')
    else:
        return redirect('login')