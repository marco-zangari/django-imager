"""Imager profile view classes."""
from django.contrib.auth.models import User
from django.views.generic import UpdateView, DetailView
from django.urls import reverse_lazy
from imager_profile.models import ImagerProfile
from imager_profile.forms import EditProfileForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class ProfileView(DetailView):
    """Profile view handling."""

    template_name = 'imager_profile/profile.html'
    model = ImagerProfile
    slug_field = 'user__username'
    slug_url_kwarg = 'username'
    context_object_name = 'profile'


class MyprofileView(DetailView):
    """Handle my profie view request."""

    template_name = 'imager_profile/profile.html'
    model = ImagerProfile
    context_object_name = 'profile'

    def get_object(self):
        return self.request.user.profile


class EditProfileView(UpdateView, LoginRequiredMixin):
    """Edit single profile."""

    login_required = True
    template_name = 'imager_profile/edit_profile.html'
    model = ImagerProfile
    form_class = EditProfileForm
    success_url = reverse_lazy('my_profile')
    context_object_name = 'profile'

    def get_object(self):
        return self.request.user.profile