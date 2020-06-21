from django_filters import CharFilter, ChoiceFilter, FilterSet, ModelChoiceFilter

import models


class ChampionFilter(FilterSet):
    name = CharFilter(label="Name", lookup_expr="icontains")
    faction__alliance = ModelChoiceFilter(
        label="Alliances", queryset=models.Alliance.objects.all(),
    )

    class Meta:
        model = models.Champion
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
        label="Faction", queryset=models.Faction.objects.all(),
    )
    champion__faction__alliance = ModelChoiceFilter(
        label="Alliance", queryset=models.Alliance.objects.all(),
    )
    champion__rarity = ChoiceFilter(
        label="Rarity", choices=models.RARITIES,
    )
    location = ModelChoiceFilter(
        label="Location", queryset=models.Location.objects.all()
    )

    class Meta:
        model = models.Rating
        fields = [
            "champion__faction",
            "champion__faction__alliance",
            "champion__rarity",
            "location"
        ]


class RatingFilterWithAffinity(RatingFilter):
    champion__affinity = ModelChoiceFilter(
        label="Affinity", queryset=models.Affinity.objects.all()
    )

    class Meta:
        model = models.Rating
        fields = [
            "champion__affinity"
        ]
