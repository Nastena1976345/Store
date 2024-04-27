from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

user = get_user_model()


# class CustomUser(AbstractUser):
#   phone_number = models.CharField(max_length=18)
#    USERNAME_FIELD = 'username'
#    REQUIRED_FIELDS = ['email']
#
#    def __str__(self):
#        return f"User: {self.email} Id: {self.pk}"

class Profile(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    img = models.ImageField(upload_to="users", default="users/default.jpg")
