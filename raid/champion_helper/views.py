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


class TeamSuggestionView(MultiTableMixin, FilterView):
    """
    Display team suggestions based on the selected inputs
    """

    model = Rating
    tables = [
        # Using attrs overrides any attrs defined in the table Meta class.
        # TODO: figure out how to dynamically set the table title? Adding
        # this (attrs={"title": "Overall Best"}) doesn't work
        RatingTable,
        RatingTable,
        RatingTable,
        RatingTable,
        RatingTable,
    ]
    template_name = "champion_helper/rating_filter.html"
    table_pagination = {"per_page": 5}
    filterset_class = RatingFilter

    def get_tables_data(self):
        """
        Return an array of table_data that should be used to populate each
        table. Specifically, this will return an array containing 5 different
        querysets based off of 1 filter for the page, and apply additional
        static filters to each of the last 4 tables
        """

        self.filter = self.filterset_class(
            self.request.GET,
            queryset=super(TeamSuggestionView, self).get_tables_data(),
        )

        ratings_by_location = self.filter.qs
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
        return [
            best_overall_team,
            best_force_team,
            best_magic_team,
            best_spirit_team,
            best_void_team
        ]


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
