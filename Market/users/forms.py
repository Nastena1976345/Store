from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model


User = get_user_model()


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email")
        widgets = {
            "username": forms.TextInput(attrs={"class": "username_field"})
        }

    password = None
