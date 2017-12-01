"""Create form models for editing, creating photos, albums."""
from imager_images.models import Album, Photo
from django import forms


class AddPhotoForm(forms.ModelForm):
    """Form to add new album."""

    class Meta:
        """Form fields for adding photo."""

        model = Photo
        fields = ['title', 'description', 'published', 'photo']
        widgets = {'description': forms.Textarea()}


class AddAlbumForm(forms.ModelForm):
    """Form to add new album."""

    class Meta:
        """Form fields for adding album."""

        model = Album
        fields = ['title', 'description', 'published', 'cover_photo']
        widgets = {'description': forms.Textarea()}
