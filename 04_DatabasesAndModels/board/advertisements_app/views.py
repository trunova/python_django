from django.shortcuts import render
from django.http import HttpResponse
from advertisements_app.models import *
import random
from django.views import generic
from typing import Callable, Any
from django.core.handlers.wsgi import WSGIRequest


class AdvertisementListView(generic.ListView):
    model = Advertisement
    template_name = 'advertisements_app/advertisements.html'
    context_object_name = 'advertisements'
    queryset = Advertisement.objects.all()[:5]

class AdvertisementDetailView(generic.DetailView):
    model = Advertisement

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        Advertisement.objects.get(id=1).views_count += 1
        return context
