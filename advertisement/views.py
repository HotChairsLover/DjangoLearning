import random

from django.shortcuts import render
from django.views import View, generic
from django.http import HttpResponse
from advertisement.models import *

#advertisements = ["Продам гараж", "Продам отель", "Продам собаку", "Куплю Олега"]
advertisements_add_count = 0
categories = ["Мебель", "Недвижимость", "Что-то"]
regions = ["Москва", "Пермь", "СПБ"]



class AdvertisementDetailed(View):

    def get(self, request):
        random_advertisement = Advertisement.objects.filter(id=random.randrange(1, Advertisement.objects.last().id + 1)).get()

        return render(request, "advertisement/post.html", {"advertisement": random_advertisement})


class AdvertisementListView(generic.ListView):
    model = Advertisement
    context_object_name = "advertisements"


class AdvertisementDetailView(generic.DetailView):
    model = Advertisement
    template_name = "advertisement/post.html"


class AdvertisementFilter(View):

    def get(self, request):
        return render(request, "advertisement/index.html", {"categories": categories,
                                                     "regions": regions})




class Regions(View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.regions = ["Москва", "Пермь", "СПБ"]

    def get(self, request):
        return render(request, "advertisement/regions.html", {'regions': self.regions})

    def post(self, request):
        region = request.POST.get("region")
        self.regions.append(region)
        return render(request, "advertisement/regions.html", {'regions': self.regions})


def advertisement_categories(resuqest, *args, **kwargs):
    categories = ["Первая", "Вторая", "Третья"]
    return render(resuqest, "advertisement/categories.html", {"categories": categories})
