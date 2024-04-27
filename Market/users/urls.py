from django.urls import path, include
from django.contrib.auth.views import PasswordChangeView
from . import views

urlpatterns = [
    path('sign_up', views.sign_up, name='sign_up'),
    path('login', views.user_login, name='login'),
    path('logout', views.user_logout, name='logout'),
    path('profile', views.user_profile, name='profile'),
    path('change_profile', views.user_change, name='change_profile'),
    path('change_password', PasswordChangeView.as_view(template_name="user/change_password.html"),
         name='change_password'),

]
