from django.shortcuts import render
from django.views import View
from django.http import HttpResponse


def advertisement_list(request, *args, **kwargs):
    return render(request, "advertisement/advertisement_list.html", {})


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
