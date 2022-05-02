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


    def get(self, request, *args, **kwargs):
        serie = self.get_object()
        serie.views += 1
        serie.save()
        return super(Details, self).get(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        context = super(Details, self).get_context_data(**kwargs)
        related = self.model.objects.filter(category=self.get_object().category)[0:5]
        context ['related'] = related
        return context


class Search (ListView):
    template_name = 'search.html'
    model = Serie

    def get_queryset(self):
        query = self.request.GET.get('query')
        if query:
            object_list = self.model.objects.filter(title__icontains=query)
            return object_list
        else:
            return None
