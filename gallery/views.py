from django.views.generic import ListView
from gallery.models import Photo

# Create your views here.


class HomePageView(ListView):
    """Homepage View.
    Retrieve random selection of photos and render them with a list view.
    """

    context_name = "random_images"
    model = Photo
    template_name = "gallery/homepage.html"
