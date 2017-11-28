from django.test import TestCase

# Create your tests here.

from imager_profile.models import User
import factory
from imager_images.models import Album, Photo
from datetime import datetime


class UserFactory(factory.django.DjangoModelFactory):
    """Factory boy!"""
    class Meta:
        model = User


class ProfileTests(TestCase):
    """Testing for the imager_image app."""

    def setUp(self):  # like a fixture, run for every time. To run once do class setUp(self):
        """Initiate with two users in the db, one activce and one not."""
        user = UserFactory.build()
        user.username = 'john'
        user.email = 'john@image.com'
        user.set_password('password')
        user.save()
        album = Album(title='Album1', owner=user.profile)
        album.save()  # to access this: user.profile.albums.first()
        photo = Photo(title='Photo1', owner=user.profile)
        photo.save()  # to access this: user.profile.photos.first()
        album.photos.add(photo)  # auto save after adding

        user = UserFactory.build()
        user.username = 'nick'
        user.email = 'nick@image.com'
        user.set_password('password')
        user.save()
        album = Album(title='Album2', owner=user.profile)
        album.save()  # to access this: user.profile.albums.first()
        photo = Photo(title='Photo2', owner=user.profile)
        photo.save()  # to access this: user.profile.photos.first()
        album.photos.add(photo)

    def test_user_nick_has_album_in_profile(self):
        """Test user have profile attribute album."""
        nick = User.objects.get(email='nick@image.com')
        self.assertIsNotNone(nick.profile.albums.first())

    def test_user_john_has_photo_in_profile(self):
        """Test user have profile attribute photo."""
        john = User.objects.get(email='john@image.com')
        self.assertIsNotNone(john.profile.photos.first())

    def test_user_nick_has_photo_in_profile(self):
        """Test user have profile attribute photo."""
        nick = User.objects.get(email='nick@image.com')
        self.assertIsNotNone(nick.profile.photos.first())

    def test_user_john_photo_has_create_date(self):
        """Test photo has an upload date."""
        john = User.objects.get(email='john@image.com')
        self.assertIsInstance(john.profile.photos.first().date_uploaded, datetime)

    def test_user_nick_photo_has_create_date(self):
        """Test photo has an upload date."""
        nick = User.objects.get(email='nick@image.com')
        self.assertIsInstance(nick.profile.photos.first().date_uploaded, datetime)

    def test_user_john_photo_has_publised_type(self):
        """Test photo has an published type."""
        john = User.objects.get(email='john@image.com')
        self.assertEquals(john.profile.photos.first().published, 'PRIVATE')

    def test_user_nick_photo_has_published_type(self):
        """Test photo has an published type."""
        nick = User.objects.get(email='nick@image.com')
        self.assertEquals(nick.profile.photos.first().published, 'PRIVATE')

    def test_user_john_album_has_create_date(self):
        """Test album has an upload date."""
        john = User.objects.get(email='john@image.com')
        self.assertIsInstance(john.profile.albums.first().date_uploaded, datetime)

    def test_user_nick_album_has_create_date(self):
        """Test album has an upload date."""
        nick = User.objects.get(email='nick@image.com')
        self.assertIsInstance(nick.profile.albums.first().date_uploaded, datetime)

    def test_user_john_album_has_publised_type(self):
        """Test album has an published type."""
        john = User.objects.get(email='john@image.com')
        self.assertEquals(john.profile.albums.first().published, 'PRIVATE')

    def test_user_nick_album_has_published_type(self):
        """Test album has an published type."""
        nick = User.objects.get(email='nick@image.com')
        self.assertEquals(nick.profile.albums.first().published, 'PRIVATE')
