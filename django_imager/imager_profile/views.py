"""."""

from django.shortcuts import render

# Create your views here.


def home_view(request):
    """View for the home view."""
    context = {'page': 'home'}
    return render(request, 'imager_profile/home.html', context=context)
