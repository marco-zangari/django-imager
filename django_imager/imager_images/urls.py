from django.conf.urls import url
from imager_images.views import library_view, album_view, photo_view, albums_view, photos_view

urlpatterns = [
    url(r'^$', library_view, name='library'),
    url(r'albums$', albums_view, name='albums'),
    url(r'photos$', photos_view, name='photos'),
    url(r'album/(?P<album_id>\d+)/$', album_view, name='album'),
    url(r'photo/(?P<photo_id>\d+)/$', photo_view, name='photo'),
]