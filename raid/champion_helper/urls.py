from django.urls import path

from . import views, models, tables, filters

# sets the application namespace
app_name = "champion_helper"

urlpatterns = [
    path("", views.GenericFilteredTableView.as_view(
        model=models.Champion,
        table_class=tables.ChampionTable,
        template_name="champion_helper/champion_filter.html",
        filter_class=filters.ChampionFilter,
    ), name="index"),
    path("teams", views.TeamSuggestionView.as_view(), name="teams"),
    
]
