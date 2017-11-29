"""View controller."""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from imager_profile.models import ImagerProfile
# Create your views here.


def home_view(request):
    """View for the home view."""
    profile = ImagerProfile.active.filter(user__username=request.user.username).first()
    try:
        photo = profile.photos.all()[0]
    except Exception:
        photo = None
    context = {'page': 'home', 'photo': photo}
    return render(request, 'imagersite/home.html', context=context)


