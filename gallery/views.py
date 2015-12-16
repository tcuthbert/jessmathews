from django.views.generic import ListView
from zinnia.models.entry import Entry
from zinnia.views.entries import *
from zinnia.feeds import EntryFeed

# Create your views here.


class HomePage(ListView):
    template_name = "gallery/homepage.html"
    queryset = Entry.published.all

# class HomePage(ListView):
    # model = EntryFeed
    # template_name = "gallery/homepage.html"
