from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth import login, authenticate, logout
from .models import Profile
from django.contrib.auth.decorators import login_required
from cart.models import Cart
from.forms import CustomUserChangeForm

def sign_up(requests):
    if requests.method == "POST":
        form = UserCreationForm(requests.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            Cart.objects.create(user=user)
            login(requests, user)
            return redirect("profile")
    else:
        form = UserCreationForm()
    return render(requests, "user/sign_up.html", {"form": form})


def user_login(requests):
    if requests.method == "POST":
        form = AuthenticationForm(data=requests.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(requests, user)
                return redirect("profile")
    else:
        form = AuthenticationForm()
    return render(requests, "user/login.html", {"form": form})


def user_change(requests):
    if requests.method == "POST":
        form = CustomUserChangeForm(requests.POST, instance=requests.user)
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = CustomUserChangeForm(instance=requests.user)
    return render(requests, "user/change_profile.html", {"form": form})


def user_logout(requests):
    logout(requests)
    return redirect("login")


@login_required
def user_profile(requests):
    profile = Profile.objects.get(user=requests.user)
    return render(requests, "user/profile.html", {"profile": profile})
