from django.shortcuts import render

from django.views import generic
from django_tables2 import SingleTableView

from .models import Champion
from .tables import ChampionTable


# Create your views here.
class IndexView(generic.ListView):
    template_name = "champion_helper/index.html"

    def get_queryset(self):
        """
        Returns all of the Champions ordered by their 'name'
        """
        order = "name"

        return Champion.objects.all().order_by(order)


class ChampionListView(SingleTableView):
    model = Champion
    table_class = ChampionTable
    template_name = "champion_helper/champs.html"
