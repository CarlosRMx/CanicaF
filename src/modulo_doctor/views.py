from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import generic
from .models import Evaluacion_Medica


class Evaluacion_MedicaListView(generic.ListView):
    model = Evaluacion_Medica
    template_name = "list_doctor.html"
