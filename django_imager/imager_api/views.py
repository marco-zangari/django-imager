"""API view class."""
from imager_images.models import Album
from imager_api.serializers import AlbumSerializer
from imager_api.permissions import IsOwnerOrReadOnly
from rest_framework import permissions
from rest_framework import generics


# Create your views here.


class AlbumDetail(generics.ListAPIView):
    """Album API handling function."""

    model = Album
    serializer_class = AlbumSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly,)

    def get_queryset(self):
        """Return proper queryset(album with curr logined user)."""
        return self.request.user.profile.albums
