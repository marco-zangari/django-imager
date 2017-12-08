from django import forms
from imager_profile.models import ImagerProfile


class EditProfileForm(forms.ModelForm):
    """Form to edit an album."""

    class Meta:
        """Fields for editing profile."""

        model = ImagerProfile
        fields = ['website', 'location', 'camera', 'fee', 'phone', 'photo_styles']