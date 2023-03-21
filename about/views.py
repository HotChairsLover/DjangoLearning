from django.shortcuts import render
from django.views.generic import TemplateView


class About(TemplateView):
    template_name = "about/index.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Название компании"
        context["desc"] = "Описание компанииииииииииии"

        return context
