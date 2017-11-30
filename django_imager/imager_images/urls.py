from django.conf.urls import url
from imager_images.views import library_view, album_view, albums_view, photos_view
from imager_images.views import PhotoDetailView

urlpatterns = [
    url(r'^$', library_view, name='library'),
    url(r'library/$', library_view, name='library'),
    url(r'albums$', albums_view, name='albums'),
    url(r'photos$', photos_view, name='photos'),
    url(r'album/(?P<album_id>\d+)/$', album_view, name='album'),
    url(r'photo/(?P<pk>\d+)/$', PhotoDetailView.as_view(), name='photo'),
]