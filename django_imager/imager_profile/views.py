"""."""

from django.shortcuts import render
from django.http import HTTPResponse
# Create your views here.

def home_view(request):
    """View for the home view."""
    return HTTPResponse('You are on the homepage')