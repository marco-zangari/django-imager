"""Profile View controller."""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.


def profile_view(request, name=None):
    """View for the home view."""
    context = {'name': name}
    return render(request, 'imagersite/profile.html', context=context)


def my_profile_view(request, name=None):
    """View for personal profile page."""
    context = {}
    return render(request, 'imagersite/my_profile.html', context=context)
