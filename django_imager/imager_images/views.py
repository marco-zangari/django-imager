"""Imager View controller."""

from imager_profile.models import ImagerProfile
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView
from imager_images.models import Album, Photo
from imager_images.forms import AddPhotoForm, AddAlbumForm, EditPhotoForm, EditAlbumForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render

# Create your views here.


def library_view(request):
    """Handle library view request."""
    profile = ImagerProfile.active.filter(user__username=request.user.username).first()
    photos = profile.photos.order_by('id')
    albums = profile.albums.order_by('id')
    album_page = request.GET.get("album_page", 1)
    photo_page = request.GET.get("photo_page", 1)
    username = request.user.username

    album_pages = Paginator(albums, 2)
    photo_pages = Paginator(photos, 4)
    try:
        albums = album_pages.page(album_page)
        photos = photo_pages.page(photo_page)
    except PageNotAnInteger:
        albums = album_pages.page(1)
        photos = photo_pages.page(1)
    except EmptyPage:
        albums = album_pages.page(album_pages.num_pages)
        photos = photo_pages.page(photo_pages.num_pages)
    return render(request, 'imager_images/library.html', {'photos': photos, 'albums': albums, 'username': username})


class AlbumView(ListView, UserPassesTestMixin):
    """Handle single album view request."""

    template_name = 'imager_images/album.html'
    context_object_name = "photos"
    paginate_by = 2
    model = Album

    def test_func(self):
        """Set permission param for page."""
        album = Album.objects.get(id=self.kwargs['album_id'])
        return self.request.user is album.owner.user or album.published == 'PUBLIC'

    def get_context_data(self):
        """Return proper context."""
        # import pdb; pdb.set_trace()
        context = super(AlbumView, self).get_context_data()
        album = Album.objects.get(id=self.kwargs['album_id'])
        photos = album.photos.all()
        context['album'] = album
        context['photo'] = photos
        return context

    def get_queryset(self):
        """Override get_query."""
        album = Album.objects.get(id=self.kwargs['album_id'])
        return album.photos.order_by('id')


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
        context = super(PhotosView, self).get_context_data()
        photos = Photo.objects.all().filter(published='PUBLIC')
        context['photos'] = photos
        return context

    def get_queryset(self):
        """Override get_query."""
        photos = Photo.objects.all()
        return photos.order_by('id')


class AddPhotoView(CreateView, LoginRequiredMixin):
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


class AddAlbumView(CreateView, LoginRequiredMixin):
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


class EditPhotoView(UpdateView, LoginRequiredMixin):
    """Edit photo view handling."""

    login_required = True
    template_name = 'imager_images/edit_photo.html'
    model = Photo
    form_class = EditPhotoForm
    success_url = reverse_lazy('library')


class EditAlbumView(UpdateView, LoginRequiredMixin):
    """docstring for EditAlbumView."""

    login_required = True
    template_name = 'imager_images/edit_album.html'
    model = Album
    form_class = EditAlbumForm
    success_url = reverse_lazy('library')
