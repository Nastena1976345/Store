from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model
from . import models

User = get_user_model()


class CustomUserChangeForm(UserChangeForm):
    photo = forms.ImageField(label='Изображение', required=False)

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email")
        widgets = {
            "username": forms.TextInput(attrs={"class": "username_field"}),
            "first_name": forms.TextInput(attrs={"placeholder": "имя"}),
            "last_name": forms.TextInput(attrs={"placeholder": "фамилия"}),
        }

    password = None

    def save(self, commit=True):
        img = self.cleaned_data.get('photo')
        user = super().save(commit)
        u_profile = models.Profile.objects.get(user=user)
        u_profile.img = img
        u_profile.save()
        return user
