from django.shortcuts import render
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
            except IntegrityError:
                error = "Такий користовач вже існує"
        else:
            error = "Паролі не співпадають"
    return render(request, 'user_app/registration.html', context={"error": error})