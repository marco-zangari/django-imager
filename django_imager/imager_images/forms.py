"""Create form models for editing, creating photos, albums."""
from imager_images.models import Album, Photo
from django import forms


class AddAlbumForm(forms.ModelForm):
    """Form to add new album."""

    def __init__(self, *args, **kwargs):
        """."""
        super(AddAlbumForm, self).__init__(*args, **kwargs)
        self.fields["cover_photo"].queryset = self.fields['owner'].queryset.first().photos.all()
        self.fields["photos"].queryset = self.fields['owner'].queryset.first().photos.all()
        del self.fields['owner']

    class Meta:
        """Define model and stuff."""

        model = Album
        exclude = [
            'date_uploaded',
            'date_modified',
            'date_published',
        ]