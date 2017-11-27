"""Test for django-imager apps."""
from django.test import TestCase

# Create your tests here.

from imager_profile.models import ImagerProfile, User
import factory
from imager_images.models import Album, Photo
from datetime import datetime


class UserFactory(factory.django.DjangoModelFactory):
    """Factory boy!"""
    class Meta:
        model = User


class ProfileTests(TestCase):
    """Testing for the imager_profile app/model."""

    def setUp(self):
        """Initiate with two users in the db, one activce and one not."""
        user = UserFactory.create()
        user.username = 'john'
        user.email = 'john@image.com'
        user.set_password('password')
        user.save()
        user.profile.website = 'www.iphoto.com'
        user.profile.camera = 'Nikkon'
        user.profile.location = 'studio destiny'
        user.profile.bio = 'I take pictures'
        user.profile.phone = '(000) 111 2222'
        user.profile.save()
        album = Album(title='Album1', owner=user.profile)
        album.save()  # to access this: user.profile.albums.first()
        photo = Photo(title='Photo1', owner=user.profile)
        photo.save()  # to access this: user.profile.photos.first()

        user = UserFactory.create()
        user.username = 'nick'
        user.email = 'nick@image.com'
        user.set_password('password')
        user.save()
        user.profile.website = 'www.imgluv.com'
        user.profile.camera = 'Sony'
        user.profile.location = 'studio hell'
        user.profile.bio = 'I take pictures too'
        user.profile.phone = '(000) 222 3333'
        user.profile.save()
        album = Album(title='Album2', owner=user.profile)
        album.save()  # to access this: user.profile.albums.first()
        photo = Photo(title='Photo2', owner=user.profile)
        photo.save()  # to access this: user.profile.photos.first()

    def test_user_nick_can_point_to_its_profile(self):
        """Test if user can point to its profile."""
        nick = User.objects.get(email='nick@image.com')
        self.assertIsNotNone(nick.profile)

    def test_user_john_can_point_to_its_profile(self):
        """Test if user can point to its profile."""
        john = User.objects.get(email='john@image.com')
        self.assertIsNotNone(john.profile)

    def test_user_nick_has_camera_in_profile(self):
        """Test user have profile attribute camera."""
        nick = User.objects.get(email='nick@image.com')
        self.assertIsNotNone(nick.profile.camera)
        self.assertEquals(nick.profile.camera, 'Sony')

    def test_user_john_has_camera_in_profile(self):
        """Test user have profile attribute camera."""
        nick = User.objects.get(email='john@image.com')
        self.assertIsNotNone(nick.profile.camera)
        self.assertEquals(nick.profile.camera, 'Nikkon')

    def test_user_john_has_website_in_profile(self):
        """Test user have profile attribute website."""
        john = User.objects.get(email='john@image.com')
        self.assertIsNotNone(john.profile.website)
        self.assertEquals(john.profile.website, 'www.iphoto.com')

    def test_user_nick_has_website_in_profile(self):
        """Test user have profile attribute website."""
        nick = User.objects.get(email='nick@image.com')
        self.assertIsNotNone(nick.profile.website)
        self.assertEquals(nick.profile.website, 'www.imgluv.com')

    def test_user_john_has_location_in_profile(self):
        """Test user have profile attribute location."""
        john = User.objects.get(email='john@image.com')
        self.assertIsNotNone(john.profile.location)
        self.assertEquals(john.profile.location, 'studio destiny')

    def test_user_nick_has_location_in_profile(self):
        """Test user have profile attribute location."""
        nick = User.objects.get(email='nick@image.com')
        self.assertIsNotNone(nick.profile.location)
        self.assertEquals(nick.profile.location, 'studio hell')

    def test_user_john_has_phone_in_profile(self):
        """Test user have profile attribute phone."""
        john = User.objects.get(email='john@image.com')
        self.assertIsNotNone(john.profile.phone)
        self.assertEquals(john.profile.phone, '(000) 111 2222')

    def test_user_nick_has_phone_in_profile(self):
        """Test user have profile attribute phone."""
        nick = User.objects.get(email='nick@image.com')
        self.assertIsNotNone(nick.profile.phone)
        self.assertEquals(nick.profile.phone, '(000) 222 3333')

    def test_user_john_has_bio_in_profile(self):
        """Test user have profile attribute bio."""
        john = User.objects.get(email='john@image.com')
        self.assertIsNotNone(john.profile.bio)

    def test_user_nick_has_bio_in_profile(self):
        """Test user have profile attribute bio."""
        nick = User.objects.get(email='nick@image.com')
        self.assertIsNotNone(nick.profile.bio)

    def test_user_john_has_album_in_profile(self):
        """Test user have profile attribute album."""
        john = User.objects.get(email='john@image.com')
        self.assertIsNotNone(john.profile.albums.first())

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
