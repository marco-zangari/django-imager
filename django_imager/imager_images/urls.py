from django.conf.urls import url
from imager_images.views import PhotoDetailView, AlbumsView, PhotosView, AlbumView, library_view, AddPhotoView, AddAlbumView, EditAlbumView, EditPhotoView

urlpatterns = [
    url(r'^$', library_view, name='library'),
    url(r'library/$', library_view, name='library'),
    url(r'albums$', AlbumsView.as_view(), name='albums'),
    url(r'photos$', PhotosView.as_view(), name='photos'),
    url(r'album/(?P<album_id>\d+)/$', AlbumView.as_view(), name='album'),
    url(r'photo/(?P<pk>\d+)/$', PhotoDetailView.as_view(), name='photo'),
    url(r'photos/add$', AddPhotoView.as_view(), name='add_photo'),
    url(r'albums/add$', AddAlbumView.as_view(), name='add_album'),
    url(r'photos/(?P<pk>\d+)/edit/$', EditPhotoView.as_view(), name='edit_photo'),
    url(r'albums/(?P<pk>\d+)/edit/$', EditAlbumView.as_view(), name='edit_album'),
]
