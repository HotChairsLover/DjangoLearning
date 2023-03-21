from django.shortcuts import render


def contacts_post(request, *args, **kwargs):
    info = {"phone": "88005553535", "email": "mail@mail.com"}
    return render(request, "contacts/index.html", {'data': info})
