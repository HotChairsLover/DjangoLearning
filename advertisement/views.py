from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

advertisements = ["Продам гараж", "Продам отель", "Продам собаку", "Куплю Олега"]
advertisements_add_count = 0


class AdvertisementList(View):

    def get(self, request):
        return render(request, "advertisement/advertisement_list.html", {"advertisements": advertisements,
                                                                         "advertisements_add_count": advertisements_add_count})

    def post(self, request):
        global advertisements_add_count
        advertisements.append(request.POST.get("advertisement"))
        advertisements_add_count += 1
        return render(request, "advertisement/advertisement_list.html", {"advertisements": advertisements,
                                                                         "advertisements_add_count": advertisements_add_count})


def advertisement_post(resuqest, *args, **kwargs):
    return render(resuqest, "advertisement/post.html", {})


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
