"""Model class."""
from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver


class ActiveUsersManger(models.Manager):
    """Active user."""
    def get_queryset(self):
        """Get the query set of active users."""
        return super(ActiveUsersManger, self).get_queryset().filter(user__is_active=True)


# Create your models here.
class ImagerProfile(models.Model):
    """Profile for the user of the application."""
    website = models.URLField(max_length=200, blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    fee = models.FloatField(max_length=200, blank=True, null=True)
    camera = models.CharField(max_length=200, blank=True, null=True)
    services = models.CharField(max_length=200, blank=True, null=True)
    bio = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=200, blank=True, null=True)
    photo_styles = models.CharField(max_length=200, blank=True, null=True)
    user = models.OneToOneField(User, related_name='profile')
    objects = models.Manager()
    active = ActiveUsersManger()

    @property
    def is_active(self):
        """Give permission to become an active user, loggin in."""
        return self.user.is_active

    def __str__(self):
        """."""
        return self.user.username


@receiver(post_save, sender=User)
def profile_generator(sender, instance, **kwargs):
    """Generate profile for user being created."""
    if kwargs['created']:
        profile = ImagerProfile(user=instance)
        profile.save()
