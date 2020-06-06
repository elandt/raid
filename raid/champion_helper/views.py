from django_tables2.views import SingleTableMixin
from django_filters.views import FilterView

from .models import Champion
from .tables import ChampionTable
from .filters import ChampionFilter


# Create your views here.
class IndexView(SingleTableMixin, FilterView):
    model = Champion
    table_class = ChampionTable
    template_name = "champion_helper/index.html"

    filterset_class = ChampionFilter
