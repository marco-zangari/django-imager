"""URL for the application imager_profile."""
from django.conf.urls import url
from imager_profile.views import profile_view


urlpatterns = [
    url(r'^(?P<user_name>\w+)', profile_view, name='profile'),
    url(r'^$', profile_view, {'user_name': 'SELF'}, name='profile')
]
