from django.views.generic import ListView
from zinnia.models.entry import Entry

# Create your views here.


class HomePage(ListView):
    model = Entry
    template_name = "gallery/homepage.html"
