"""URL for the application imager_profile."""
from django.conf.urls import url

import views

urlpatterns = [
    url(r'^$', views.home_view, name='home'),
]
