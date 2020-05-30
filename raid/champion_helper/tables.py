import django_tables2 as tables
from .models import Champion


class ChampionTable(tables.Table):
    ratings = tables.Column(accessor=tables.A("rating_set.all"))

    class Meta:
        model = Champion
        template_name = "django_tables2/bootstrap4.html"
        fields = (
            "name",
            "faction",
            "faction.alliance",
            "rarity",
            "affinity",
            "type",
            "avg_rating"
        )
        attrs = {"class": "table table-striped table-dark"}
