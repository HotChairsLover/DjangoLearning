from django.shortcuts import render


def about_post(request, *args, **kwargs):
    info = {"title": "Название компании", "desc": "Описание компании"}
    return render(request, "about/index.html", {'data': info})
