from django.urls import path

from . import views

# sets the application namespace
app_name = "champion_helper"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("champs/", views.ChampionListView.as_view(), name="champs"),
]
