from django_filters import FilterSet

from .models import Champion


class ChampionFilter(FilterSet):
    class Meta:
        model = Champion
        fields = {
            'name': ['icontains'],
            'type': ['icontains'],
            # 'faction': ['icontains'],
            # 'faction__alliance': ['icontains'],
            'rarity': ['icontains']
        }