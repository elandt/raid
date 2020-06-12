import django_tables2 as tables
from django.db.models import Avg

from decimal import Decimal

from .models import Champion, Rating


class ChampionTable(tables.Table):
    avg_rating = tables.Column(verbose_name="Average Rating")
    # TODO: Determine if there's a sensible way to
    # sort this column, or is disabling sorting the
    # best option?
    ratings = tables.TemplateColumn(
        template_name="champion_helper/rating_list.html",
        orderable=False,
    )

    def render_avg_rating(self, value):
        """
        Rounds the display of the Average Rating to 1 decimal place.
        """
        return Decimal(value).quantize(Decimal("1.0"))

    # Relevant documentation/resources:
    # Django's annotate() - https://docs.djangoproject.com/en/3.0/ref/models/querysets/#annotate
    # Django's Avg - https://docs.djangoproject.com/en/3.0/ref/models/querysets/#avg
    # Django-tables2 custom ordering - https://django-tables2.readthedocs.io/en/latest/pages/ordering.html#table-order-foo-methods
    # Stack Overflow questions -
    # https://stackoverflow.com/q/12614779/3570769
    # https://stackoverflow.com/q/48397761/3570769
    def order_avg_rating(self, queryset, is_descending):
        """
        Enables the Average Rating table column to
        be sortable. The average is returned, and
        sorted as a float.
        """
        queryset = queryset.annotate(avg_rating=Avg("rating__value")).order_by(
            ("-" if is_descending else "") + "avg_rating"
        )
        return (queryset, True)

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
        attrs = {"class": "table table-striped table-dark tableFixHead"}


class RatingTable(tables.Table):
    class Meta:
        model = Rating
        template_name = "django_tables2/bootstrap4.html"
        fields = (
            "champion.name",
            "champion.faction",
            "champion.faction.alliance",
            "champion.rarity",
            "champion.affinity",
            "champion.type",
            "location",
            "value",
        )
        attrs = {"class": "table table-striped table-dark tableFixHead"}
