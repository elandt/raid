from django_tables2.views import SingleTableMixin, SingleTableView, MultiTableMixin
from django_filters.views import FilterView

from .models import Champion, Rating
from .tables import ChampionTable, RatingTable
from .filters import ChampionFilter, RatingFilter


# Create your views here.
class IndexView(SingleTableMixin, FilterView):
    model = Champion
    table_class = ChampionTable
    template_name = "champion_helper/index.html"

    filterset_class = ChampionFilter


# TODO: probably don't need FilterView here because it
# would be a form for all of the tables


class TeamSuggestionView(MultiTableMixin, FilterView):
    """
    Display team suggestions based on the selected inputs
    """

    model = Rating

    # TODO: Filter displays, but does nothing...need to figure out
    # why, and how to fix it.
    filterset_class = RatingFilter

    # TODO: Figure out what this should actually be. Need to apply
    # sanitized input from a form
    ratings_by_location = Rating.objects.all()
    best_overall_team = ratings_by_location
    best_force_team = ratings_by_location.filter(
        champion__affinity__name="force"
    )
    best_magic_team = ratings_by_location.filter(
        champion__affinity__name="magic"
    )
    best_spirit_team = ratings_by_location.filter(
        champion__affinity__name="spirit"
    )
    best_void_team = ratings_by_location.filter(
        champion__affinity__name="void",
    )

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
        RatingTable(best_void_team),
    ]
    template_name = "champion_helper/teams.html"

    table_pagination = {"per_page": 5}


class GenericFilteredTableView(SingleTableView):
    filter_class = None

    def get_table_data(self):
        self.filter = self.filter_class(
            self.request.GET,
            queryset=super(GenericFilteredTableView, self).get_table_data(),
        )
        return self.filter.qs

    def get_context_data(self, **kwargs):
        context = super(
            GenericFilteredTableView,
            self
        ).get_context_data(**kwargs)
        context["filter"] = self.filter
        return context
