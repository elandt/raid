from django.contrib import admin

from .models import Affinity, Alliance, Champion, Faction, Rating
# Register your models here.


@admin.register(Affinity)
class AffintyAdmin(admin.ModelAdmin):

    empty_value_display = "-empty-"
    list_display = ("name", "strength", "weakness")


@admin.register(Alliance, Faction)
class AllianceFactionAdmin(admin.ModelAdmin):
    # TODO: figure out how I want to customize this.
    pass


# TODO: I'll probably want to customize these admin pages later.
raid_helper_models = [Champion, Rating]
admin.site.register(raid_helper_models)
