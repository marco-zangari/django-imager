"""Profile View controller."""

from django.contrib.auth.models import User
from django.shortcuts import render
from imager_profile.models import ImagerProfile


# Create your views here.


def profile_view(request, user_name=None):
    """View for the home view."""
    if user_name == 'SELF':
        user_name = request.user.username
    profile = ImagerProfile.active.get(user__username=user_name)
    user = User.objects.filter(username=user_name).first()
    user.profile.camera = 'testing camera'
    user.profile.bio = 'testing bio'
    photo = profile.photos.all()
    context = {'photos': photo, 'profile': profile, 'userdata': user}
    return render(request, 'imager_profile/profile.html', context=context)

