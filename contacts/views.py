from django.shortcuts import render
from django.views.generic import TemplateView


class Contacts(TemplateView):
    template_name = "contacts/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["phone"] = "88005553535"
        context["email"] = "mail@mail.ru"

        return context
