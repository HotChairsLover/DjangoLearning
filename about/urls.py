from django.urls import path
from .import views

urlpatterns = [
    path("", views.about_post, name='about_index'),
]
