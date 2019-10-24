from django.urls import path

from . import views

app_name="nino"
urlpatterns = [
    path("",views.NNAListView.as_view(),name="list"),
    path("A_dental/",views.Area_DentalListView.as_view(),name="list_dental"),
]