from django_filters import CharFilter, ChoiceFilter, FilterSet, ModelChoiceFilter

from .models import Alliance, Champion, Faction, Location, Rating, RARITIES


class ChampionFilter(FilterSet):
    name = CharFilter(label="Name", lookup_expr="icontains")
    faction__alliance = ModelChoiceFilter(
        label="Alliances", queryset=Alliance.objects.all(),
    )

    class Meta:
        model = Champion
        fields = [
            "name",
            "faction",
            "faction__alliance",
            "rarity",
            "affinity",
            "type"
        ]


class RatingFilter(FilterSet):
    champion__faction = ModelChoiceFilter(
        label="Faction", queryset=Faction.objects.all(),
    )
    champion__faction__alliance = ModelChoiceFilter(
        label="Alliance", queryset=Alliance.objects.all(),
    )
    champion__rarity = ChoiceFilter(
        label="Rarity", choices=RARITIES,
    )
    location = ModelChoiceFilter(
        label="Location", queryset=Location.objects.all()
    )

    class Meta:
        model = Rating
        fields = [
            "champion__faction",
            "champion__faction__alliance",
            "champion__rarity",
            "location"
        ]
