from django.shortcuts import render
from .models import Serie
from django.views.generic import TemplateView, ListView, DetailView

# Create your views here.


class Homepage (TemplateView):
    template_name = 'homepage.html'


class Homeseries (ListView):
    template_name = 'homeseries.html'
    model = Serie


class Details (DetailView):
    template_name = 'details.html'
    model = Serie

    def get_context_data(self, **kwargs):
        context = super(Details, self).get_context_data(**kwargs)
        related = Serie.objects.filter(category=self.get_object().category)[0:5]
        context ['related'] = related
        return context
