from django_tables2.views import SingleTableMixin, MultiTableMixin
from django_filters.views import FilterView

from .models import Champion, Rating
from .tables import ChampionTable, RatingTable
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
    model = Rating
    # TODO: Figure out what this should actually be. Need to apply
    # sanitized input from a form
    best_overall_team = Rating.objects.filter(location__name="dragon")[:5]
    best_force_team = Rating.objects.filter(
        champion__affinity__name="force", location__name="dragon"
    )[:5]
    best_magic_team = Rating.objects.filter(
        champion__affinity__name="magic", location__name="dragon"
    )[:5]
    best_spirit_team = Rating.objects.filter(
        champion__affinity__name="spirit", location__name="dragon"
    )[:5]
    best_void_team = Rating.objects.filter(
        champion__affinity__name="void", location__name="dragon"
    )[:5]

    # TODO: These should probably be rating based?
    tables = [
        # Using attrs overrides any attrs defined in the table Meta class.
        # TODO: figure out how to dynamically set the table title? Adding
        # this (attrs={"title": "Overall Best"}) doesn't work
        # TODO: Either need dynamic filtering of tables, or different tables
        # dynamic filtering can probably be achieved through a form,
        # and querysets?
        RatingTable(best_overall_team),
        RatingTable(best_force_team),
        RatingTable(best_magic_team),
        RatingTable(best_spirit_team),
        RatingTable(best_void_team)
    ]
    template_name = "champion_helper/teams.html"

    # filterset_class = ChampionFilter

    table_pagination = {
        "per_page": 5
    }
