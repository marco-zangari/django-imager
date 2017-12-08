from django import forms
from imager_profile.models import ImagerProfile


class EditProfileForm(forms.ModelForm):
    """Form to edit an album."""

    class Meta:
        """Fields for editing profile."""

        model = ImagerProfile
        fields = ['bio', 'website', 'location', 'camera', 'fee', 'phone', 'services', 'photo_styles']

