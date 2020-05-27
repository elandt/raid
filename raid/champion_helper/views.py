from django.shortcuts import render

from django.views import generic

from .models import Champion


# Create your views here.
class IndexView(generic.ListView):
    template_name = "champion_helper/index.html"

    def get_queryset(self):
        """

        """
        order = "name"

        return Champion.objects.all().order_by(order)
