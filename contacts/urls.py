from django.urls import path
from .import views

urlpatterns = [
    path("", views.contacts_post, name='contacts_index'),
]
