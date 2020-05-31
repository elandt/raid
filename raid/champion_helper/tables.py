import django_tables2 as tables

from .models import Champion


class ChampionTable(tables.Table):
    ratings = tables.Column(accessor=tables.A("rating_set.all"))

    def render_ratings(self, value):
        # This displays the location,
        # value, and location type for a rating,
        # but as a list of strings...
        # TODO: figure out how to get this
        # to display better
        return [
            f"{rating.location} - {rating.value} - {rating.location.type}"
            for rating in value
        ]
    
    # TODO: add custom ordering for avg_rating,
    # or disable ordering on that column

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
            "avg_rating",
        )
        attrs = {"class": "table table-striped table-dark"}
