"""Imager View controller."""

from imager_profile.models import ImagerProfile
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView
from imager_images.models import Album, Photo
from imager_images.forms import AddPhotoForm, AddAlbumForm, EditPhotoForm
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

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


class AlbumView(ListView):
    """Handle single album view request."""

    template_name = 'imager_images/album.html'

    def get_context_data(self):
        """Return proper context."""
        album = Album.objects.get(id=self.kwargs['album_id'])
        if album.published == 'PRIVATE':
            photos = album.photos.all()
            return {'album': album, 'photos': photos}

    def get_queryset(self):
        """Override get_query."""


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


class PhotosView(ListView):
    """Handle all photos view request."""

    template_name = 'imager_images/photos.html'

    def get_context_data(self):
        """Return all album instances."""
        photos = Photo.objects.all()
        return {'photos': photos}

    def get_queryset(self):
        """Override get_query."""


class AddPhotoView(CreateView):
    """Add photo view handling."""

    login_required = True
    template_name = 'imager_images/add_photo.html'
    model = Photo
    form_class = AddPhotoForm
    success_url = reverse_lazy('library')

    def form_valid(self, form):
        """If form is valid, save, assign owner and re-direct."""
        form.instance.owner = self.request.user.profile
        return super(CreateView, self).form_valid(form)


class AddAlbumView(CreateView):
    """Add album view handling."""

    login_required = True
    template_name = 'imager_images/add_album.html'
    model = Album
    form_class = AddAlbumForm
    success_url = reverse_lazy('library')

    def form_valid(self, form):
        """If form is valid, save, assign owner and re-direct."""
        form.instance.owner = self.request.user.profile
        return super(CreateView, self).form_valid(form)


class EditPhotoView(UpdateView):
    """Edit photo view handling."""

    login_required = True
    template_name = 'imager_images/edit_photo.html'
    model = Photo
    form_class = EditPhotoForm
    success_url = reverse_lazy('library')


class EditAlbumView(UpdateView):
    """docstring for EditAlbumView."""

    login_required = True
    template_name = 'imager_images/edit_album.html'
    model = Album
    form_class = EditPhotoForm
    success_url = reverse_lazy('library')

