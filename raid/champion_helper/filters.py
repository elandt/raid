from django_filters import ChoiceFilter, FilterSet, ModelChoiceFilter

from .models import Affinity, Alliance, Champion, Faction, RARITIES, TYPES


class ChampionFilter(FilterSet):
    faction = ModelChoiceFilter(
        label="Factions",
        queryset=Faction.objects.all()
    )
    alliance = ModelChoiceFilter(
        label="Alliances",
        queryset=Alliance.objects.all()
    )
    rarity = ChoiceFilter(label='Type', choices=RARITIES)
    affinity = ModelChoiceFilter(
        label='Affinities',
        queryset=Affinity.objects.all()
    )
    type = ChoiceFilter(label='Type', choices=TYPES)

    class Meta:
        model = Champion
        fields = {
            "name": ["icontains"],
        }
