import random

from django.shortcuts import render
from django.views import View
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


class AdvertisementList(View):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.advertisements = Advertisement.objects.all()

    def get(self, request):

        return render(request, "advertisement/advertisement_list.html", {"advertisements": self.advertisements,
                                                                         "advertisements_add_count": advertisements_add_count})

    def post(self, request):
        #global advertisements_add_count
        #advertisements.append(request.POST.get("advertisement"))
        #advertisements_add_count += 1
        return render(request, "advertisement/advertisement_list.html", {"advertisements": self.advertisements,
                                                                         "advertisements_add_count": advertisements_add_count})


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
