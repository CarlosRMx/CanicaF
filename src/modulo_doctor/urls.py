from django.urls import path

from . import views

app_name="modulo_doctor"
urlpatterns = [
    path("",views.Evaluacion_MedicaListView.as_view(),name="list_doctor"),
]