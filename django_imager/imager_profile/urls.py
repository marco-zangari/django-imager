"""URL for the application imager_profile."""
from django.conf.urls import url, include
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^registration/', include("registration.backends.simple.urls")),

]
