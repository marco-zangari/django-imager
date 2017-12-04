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


class EditPhotoForm(forms.ModelForm):
    """Form to edit a photo."""

    class Meta:
        """Fields for editing photo."""

        model = Photo
        fields = ['title', 'description', 'published']
        widgets = {'description': forms.Textarea()}


class EditAlbumForm(forms.ModelForm):
    """Form to edit an album."""

    class Meta:
        """Fields for editing album."""

        model = Album
        fields = ['title', 'description', 'published', 'photos', 'cover_photo']
        widgets = {'description': forms.Textarea()}

