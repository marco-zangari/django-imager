"""Model class."""
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class ImagerProfile(models.Model):
    """Profile for the user of the application."""
    is_active = models.BooleanField(default=False)
    website = models.URLField(max_length=200, blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    fee = models.FloatField(max_length=200, blank=True, null=True)
    camera = models.CharField(max_length=200, blank=True, null=True)
    services = models.CharField(max_length=200, blank=True, null=True)
    bio = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=200, blank=True, null=True)
    photo_styles = models.CharField(max_length=200, blank=True, null=True)
    user = models.OneToOneField(User, related_name='profile')

    def active(self):
        """Give permission for active user, loggin in."""
        self.is_active = True
        return
