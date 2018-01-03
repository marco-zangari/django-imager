"""URL for the application imager_profile."""
from django.conf.urls import url
from imager_profile.views import ProfileView, EditProfileView, MyprofileView


urlpatterns = [
    url(r'^$', MyprofileView.as_view(), name='my_profile'),
    url(r'edit$', EditProfileView.as_view(), name='edit_profile'),
    url(r'^(?P<username>\w+)', ProfileView.as_view(), name='profile'),

]
