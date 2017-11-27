"""Model for the images."""
from django.db import models
from imager_profile.models import ImagerProfile
from django.contrib.auth.models import User


from django.db.models.signals import post_save
from django.dispatch import receiver


class Photo(models.Model):
    """Model for each photos."""

    owner = models.ForeignKey(
        ImagerProfile,
        related_name='photos',
        on_delete=models.CASCADE,
    )

    PUBLISH_CHOICES = (
        ('PRIVATE', 'private'),
        ('SHARED', 'shared'),
        ('PUBLIC', 'public'),
    )

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200, blank=True, null=True)
    published = models.CharField(max_length=200, choices=PUBLISH_CHOICES, default='PRIVATE')
    date_uploaded = models.DateTimeField(auto_now=True)
    date_modified = models.DateTimeField(auto_now=True)
    date_published = models.DateTimeField(blank=True, null=True)
    photo = models.ImageField(upload_to='', blank=True, null=True)


class Album(models.Model):
    """Model for each album."""

    owner = models.ForeignKey(
        ImagerProfile,
        related_name='albums',
        on_delete=models.CASCADE,
    )

    photos = models.ManyToManyField(
        Photo,
        related_name='albums'
    )

    PUBLISH_CHOICES = (
        ('PRIVATE', 'private'),
        ('SHARED', 'shared'),
        ('PUBLIC', 'public'),
    )

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200, blank=True, null=True)
    published = models.CharField(max_length=150, choices=PUBLISH_CHOICES, default='PRIVATE')
    date_uploaded = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    date_published = models.DateTimeField(blank=True, null=True)
    cover_photo = models.ImageField(upload_to='', blank=True, null=True)
