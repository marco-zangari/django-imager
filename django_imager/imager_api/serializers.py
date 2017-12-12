"""Serializer for api view delivery."""
from rest_framework import serializers
from rest_framework import permissions
from imager_images.models import Album, Photo


class PhotoSerializer(serializers.ModelSerializer):
    """Photo serializer class."""

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    class Meta:
        """Adding meta data."""

        model = Photo
        fields = ('photo', 'title', 'description', 'published', 'date_uploaded')


class AlbumSerializer(serializers.ModelSerializer):
    """Photo serializer class."""

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    owner = serializers.ReadOnlyField(source='owner.username')
    photos = PhotoSerializer(many=True)

    class Meta:
        """Adding meta data."""

        model = Album
        fields = ('owner', 'title', 'description', 'photos', 'cover_photo', 'date_uploaded')


