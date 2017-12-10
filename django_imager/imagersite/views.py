"""View controller."""

from imager_images.models import Photo
from imager_profile.models import ImagerProfile
from django.views.generic import TemplateView

# Create your views here.


class HomeView(TemplateView):
    """Home View handling."""
    template_name = 'imagersite/home.html'

    def get_context_data(self):
        try:
            photo = Photo.public.all()[0]
        except Exception:
            photo = None
        return {'page': 'home', 'photo': photo}

