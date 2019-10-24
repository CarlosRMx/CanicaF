from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import generic
from .models import NNA,Area_Dental
# Create your views here.


class NNAListView(generic.ListView):
    model = NNA
    template_name = "list.html"


class NNADetailView(generic.DetailView):
    model = NNA
    template_name = "detail.html"


class Area_DentalListView(generic.ListView):
    model = Area_Dental
    template_name = "list_dental.html"

