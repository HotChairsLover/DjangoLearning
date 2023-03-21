from django.urls import path
from .import views

urlpatterns = [
    path("", views.advertisement_list, name='advertisement_list'),
    path("post", views.advertisement_post, name='advertisement_post'),
    path("categories", views.advertisement_categories, name='advertisement_categories'),
    path("regions", views.Regions.as_view()),
]
