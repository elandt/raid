from django.contrib import admin

from .models import Affinity, Alliance, Champion, Faction, Location, Rating

# Register your models here.


@admin.register(Affinity)
class AffintyAdmin(admin.ModelAdmin):
    empty_value_display = "-empty-"
    list_display = ("name", "strength", "weakness")


class FactionInline(admin.TabularInline):
    model = Faction
    fk_name = "alliance"


@admin.register(Alliance)
class AllianceFactionAdmin(admin.ModelAdmin):
    # TODO: May still want to do more customizations...
    # but good enough for now
    inlines = [FactionInline]
    empty_value_display = "-empty-"
    list_display = ("name", "factions_in_alliance")

    def factions_in_alliance(self, obj):
        """
        Returns the __str__() of all the 'Factions' in an Alliance
        """
        return [faction for faction in obj.faction_set.all()]


class RatingInline(admin.TabularInline):
    model = Rating


@admin.register(Champion)
class ChampionAdmin(admin.ModelAdmin):
    # TODO: still probably needs more customizations
    inlines = [RatingInline]
    list_display = ["__str__", "avg_rating"]
    fields = ("name", ("rarity", "faction", "affinity", "type"))


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ("__str__", "type")
