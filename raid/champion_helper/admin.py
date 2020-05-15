from django.contrib import admin

from .models import Affinity, Alliance, Champion, Faction, Ratings
# Register your models here.

# TODO: I'll probably want to customize these admin pages later.
admin.site.register(Affinity, Alliance, Champion, Faction, Ratings)
