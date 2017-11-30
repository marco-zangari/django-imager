"""Imager View controller."""

# from django.contrib.auth.models import User
from django.shortcuts import render
from imager_profile.models import ImagerProfile
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from imager_images.models import Album, Photo

# Create your views here.


class LibraryView(ListView):
    """Handle library view request."""

    template_name = 'imager_images/library.html'

    def get_context_data(self):
        """Return proper context."""
        profile = ImagerProfile.active.filter(user__username=self.request.user.username).first()
        photos = profile.photos.all()
        albums = profile.albums.all()
        username = self.request.user.username
        return {'photos': photos, 'profile': profile, 'albums': albums, 'username': username}

    def get_queryset(self):
        """Override get_query."""
        return {}


class AlbumView(ListView):
    """Handle single album view request."""

    template_name = 'imager_images/album.html'

    def get_context_data(self):
        """Return proper context."""
        album = Album.objects.get(id=self.kwargs['album_id'])
        if album.published == 'PRIVATE':
            photos = album.photos.all()
            return {'album': album, 'photos': photos}


class PhotoDetailView(DetailView):
    """Handle single photo request."""

    template_name = 'imager_images/photo.html'
    model = Photo


class AlbumsView(ListView):
    """Handle all album view request."""

    template_name = 'imager_images/albums.html'

    def get_context_data(self):
        """Return all album instances."""
        albums = Album.objects.all()
        return {'albums': albums}

    def get_queryset(self):
        """Override get_query."""
        return {}


class PhotosView(ListView):
    """Handle all photos view request."""

    template_name = 'imager_images/photos.html'

    def get_context_data(self):
        """Return all album instances."""
        photos = Photo.objects.all()
        return {'photos': photos}

    def get_queryset(self):
        """Override get_query."""
        return {}
