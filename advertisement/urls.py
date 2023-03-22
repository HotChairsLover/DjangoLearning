from django.urls import path
from .import views

urlpatterns = [
    path("advertisement", views.AdvertisementListView.as_view(), name="advertisement_list"),
    path("advertisement/<int:pk>", views.AdvertisementDetailView.as_view(), name="advertisement_detail"),
    path("post", views.AdvertisementDetailed.as_view(), name='advertisement_post'),
    path("categories", views.advertisement_categories, name='advertisement_categories'),
    path("regions", views.Regions.as_view()),
    path("", views.AdvertisementFilter.as_view())
]
