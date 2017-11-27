"""View controller."""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.


def home_view(request):
    """View for the home view."""
    context = {'page': 'home'}
    return render(request, 'imagersite/home.html', context=context)

