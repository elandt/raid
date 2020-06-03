from django.shortcuts import render

from django.views import generic
from django_tables2 import SingleTableView

from .models import Champion
from .tables import ChampionTable


# Create your views here.
class IndexView(SingleTableView):
    model = Champion
    table_class = ChampionTable
    template_name = "champion_helper/index.html"
