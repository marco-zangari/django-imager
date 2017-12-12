from rest_framework import serializers
from snippets.models import Snippet
from django.contrib.auth.models import User
from rest_framework import permissions
from imager_images.models import Album


class AlbumSerializer(serializers.ModelSerializer):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Album
        fields = ('owner', 'title', 'date_uploaded', 'photo')


class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    class Meta:
        model = User
        fields = ('id', 'username')
