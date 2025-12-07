from django.shortcuts import render
from django.contrib.auth.models import User


def render_registration(request):
    error = ""
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        password_confirm = request.POST.get("password_confirm")
        if password == password_confirm:
            User.objects.create_user(username=username, password=password)
        else:
            error = "Паролі не співпадають"
    return render(request, 'user_app/registration.html', context={"error": error})