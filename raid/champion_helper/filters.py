from django_filters import CharFilter, FilterSet, ModelChoiceFilter

from .models import Alliance, Champion


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
