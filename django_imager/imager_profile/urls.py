"""URL for the application imager_profile."""
from django.conf.urls import url, include
from django.contrib.auth.views import login, logout
from imager_profile.views import profile_view, my_profile_view


urlpatterns = [
    url(r'^(?P<name>\w+)', profile_view, name='profile'),
    url(r'^$', my_profile_view, name='my_profile_view')
]
