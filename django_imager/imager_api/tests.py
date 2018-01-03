# Create your tests here.
from django.test import TestCase, Client, RequestFactory
from django.urls import reverse_lazy
from django.core.files.uploadedfile import SimpleUploadedFile
from imager_images.tests import UserFactory, AlbumFactory, PhotoFactory


class ViewTest(TestCase):
    """Testing for the imager_api app/model."""

    def setUp(self):
        """Initiate user, with photo and album tie to him."""
        user = UserFactory.build()
        user.username = 'john'
        user.email = 'john@image.com'
        user.set_password('password')
        user.save()
        self.client = Client()

        photo = PhotoFactory.build()
        photo.owner = user.profile
        photo.title = 'test_photo'
        with open('imager_images/static/default.jpeg', 'rb') as img:  # img must be open with rb format
            photo.photo = SimpleUploadedFile('img', img.read())
        photo.save()

        album = AlbumFactory.build()
        album.owner = user.profile
        album.title = 'test_album'
        album.save()
        album.photos.add(photo)

        self.client.force_login(user)

    def test_api_album_view(self):
        """Test api album view is accessible."""
        response = self.client.get(reverse_lazy('api_album'))
        self.assertEquals(response.status_code, 200)

    def test_api_album_view_can_view_photos(self):
        """Test api album view works properly."""
        response = self.client.get(reverse_lazy('api_album'))
        self.assertTrue(b'test_photo' in response.rendered_content)

    def test_non_user_cannot_view_album_photos(self):
        """Test api album view works properly."""
        self.client.logout()
        response = self.client.get(reverse_lazy('api_album'))
        self.assertTrue(b"Authentication credentials were not provided." in response.rendered_content)
