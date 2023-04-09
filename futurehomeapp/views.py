from django.shortcuts import render
from django.views import generic
from .models import Listing


class ListingList(generic.ListView):
    model = Listing
    queryset = Listing.objects.filter(status=0).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6
