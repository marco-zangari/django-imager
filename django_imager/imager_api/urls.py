"""URL routing for API views."""
from django.conf.urls import url, include
from imager_api import views
from rest_framework.routers import DefaultRouter

# Create a router and register our viewsets with it.
router = DefaultRouter()
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^v1/albums/$', views.AlbumDetail.as_view()),
]
