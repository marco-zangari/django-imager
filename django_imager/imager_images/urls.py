from django.conf.urls import url
from imager_images.views import PhotoDetailView, AlbumsView, PhotosView, AlbumView, LibraryView, AddPhotoView, AddAlbumView

urlpatterns = [
    url(r'^$', LibraryView.as_view(), name='library'),
    url(r'library/$', LibraryView.as_view(), name='library'),
    url(r'albums$', AlbumsView.as_view(), name='albums'),
    url(r'photos$', PhotosView.as_view(), name='photos'),
    url(r'album/(?P<album_id>\d+)/$', AlbumView.as_view(), name='album'),
    url(r'photo/(?P<pk>\d+)/$', PhotoDetailView.as_view(), name='photo'),
    url(r'photos/add$', AddPhotoView.as_view(), name='add_photo'),
    url(r'albums/add$', AddAlbumView.as_view(), name='add_album')
]
