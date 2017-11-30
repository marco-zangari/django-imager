"""Imager View controller."""

# from django.contrib.auth.models import User
from django.shortcuts import render
from imager_profile.models import ImagerProfile
from django.views.generic.detail import DetailView
from imager_images.models import Album, Photo

# Create your views here.


def library_view(request):
    """Library view handling function."""
    profile = ImagerProfile.active.filter(user__username=request.user.username).first()
    photos = profile.photos.all()
    albums = profile.albums.all()
    username = request.user.username

    return render(request, 'imager_images/library.html', {'photos': photos, 'profile': profile, 'albums': albums, 'username': username})


def album_view(request, album_id):
    """Album view handling function."""
    album = Album.objects.filter(id=album_id).first()
    photos = album.photos.all()
    return render(request, 'imager_images/album.html', {'album': album, 'photos': photos})


class PhotoDetailView(DetailView):
    """Handle single photo request."""

    template_name = 'imager_images/photo.html'
    model = Photo


def albums_view(request):
    """Return all album, cover photo. Albums view handling function."""
    albums = Album.objects.all()
    return render(request, 'imager_images/albums.html', {'albums': albums})


def photos_view(request):
    """Return all photos, cover photo. photos view handling function."""
    photos = Photo.objects.all()
    return render(request, 'imager_images/photos.html', {'photos': photos})
