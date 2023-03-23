from django.urls import path

from app_users.views import *

urlpatterns = [
    path("login", UserAuth.as_view(), name="user_login"),
    path("register", UserRegister.as_view(), name="user_register"),
    path("logout", UserLogout.as_view(), name="user_logout")
]
