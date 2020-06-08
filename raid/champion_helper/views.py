from django_tables2.views import SingleTableMixin, MultiTableMixin
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


class TeamSuggestionView(MultiTableMixin, FilterView):
    """
    Display team suggestions based on the selected inputs
    """
    model = Champion
    # TODO: Figure out what this should actually be.
    qs = Champion.objects.all()
    # TODO: These should probably be rating based?
    tables = [
        # Using attrs overrides any attrs defined in the table Meta class.
        # TODO: figure out how to dynamically set the table title?
        ChampionTable(qs, attrs={"title": "Overall Best"}),
        ChampionTable(qs, attrs={"title": "Best Force Team"}),
        ChampionTable(qs, attrs={"title": "Best Magic Team"}),
        ChampionTable(qs, attrs={"title": "Best Spirit Team"}),
        ChampionTable(qs, attrs={"title": "Best Void Team"})
    ]
    template_name = "champion_helper/teams.html"

    # filterset_class = ChampionFilter

    table_pagination = {
        "per_page": 5
    }
