from django.urls import path

from . import views, models, tables, filters

# sets the application namespace
app_name = "champion_helper"

urlpatterns = [
    path("", views.GenericFilteredTableView.as_view(
        model=models.Champion,
        table_class=tables.ChampionTable,
        template_name='champion_helper/index.html',
        filter_class=filters.ChampionFilter,
    ), name='index'),
    # path("", views.IndexView.as_view(), name="index"),
    path("teams", views.TeamSuggestionView.as_view(), name="teams"),
]
