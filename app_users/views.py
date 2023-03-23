from django.contrib.auth.views import *
from django.shortcuts import render
from django.views.generic import CreateView
from app_users.forms import *


class UserAuth(LoginView):
    template_name = "app_users/login.html"


class UserLogout(LogoutView):
    next_page = "/advertisement"


class UserRegister(CreateView):
    form_class = RegisterForm
    success_url = "login"
    template_name = "app_users/register.html"
