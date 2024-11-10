from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

from .forms import RegistrationForm


def login_view(request):

    if request.user.is_authenticated:
        return redirect("index")

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("index")

    elif request.method == "GET":
        form = AuthenticationForm(request)

    return render(request, "user/login.html",
                  context={"form": form},
                  )


def logout_view(request):
    logout(request)
    return redirect("index")


def registration_view(request):
    if request.user.is_authenticated:
        return redirect("index")

    if request.method == "POST":
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    elif request.method == "GET":
        form = RegistrationForm()

    return render(request,"user/registration.html",
                  context={"form": form},
                  )
