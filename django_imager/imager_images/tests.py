from django.test import TestCase

# Create your tests here.

from imager_profile.models import User, ImagerProfile
import factory
from imager_images.models import Album, Photo
from datetime import datetime
from django.test import Client
from django.urls import reverse_lazy
from django.core.files.uploadedfile import SimpleUploadedFile


class UserFactory(factory.django.DjangoModelFactory):
    """Factory boy!"""
    class Meta:
        model = User


class PhotoFactory(factory.django.DjangoModelFactory):
    """Factory boy!"""
    class Meta:
        model = Photo


class AlbumFactory(factory.django.DjangoModelFactory):
    """Factory boy!"""
    class Meta:
        model = Album


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


class ViewTest(TestCase):
    """Testing for the imager_images app/model."""

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

    def test_can_access_library_view(self):
        """Test library view is accessible."""
        response = self.client.get(reverse_lazy('library'))
        self.assertEquals(response.status_code, 200)

    def test_can_access_photos_view(self):
        """Test all photos view is accessible."""
        response = self.client.get(reverse_lazy('photos'))
        self.assertEquals(response.status_code, 200)

    def test_can_access_albums_view(self):
        """Test all albums view is accessible."""
        response = self.client.get(reverse_lazy('albums'))
        self.assertEquals(response.status_code, 200)

    def test_can_access_album_view(self):
        """Test all album view is accessible."""
        album_id = Album.objects.last().id
        response = self.client.get(reverse_lazy('album', kwargs={'album_id': album_id}))
        self.assertEquals(response.status_code, 200)

    def test_can_access_photo_view(self):
        """Test all photo view is accessible."""
        photo_id = Photo.objects.last().id
        response = self.client.get(reverse_lazy('photo', kwargs={'pk': photo_id}))
        self.assertEquals(response.status_code, 200)

    def test_can_access_add_album_view(self):
        """Test all add album view is accessible."""
        response = self.client.get(reverse_lazy('add_album'))
        self.assertEquals(response.status_code, 200)

    def test_can_access_add_photo_view(self):
        """Test all add photo view is accessible."""
        response = self.client.get(reverse_lazy('add_photo'))
        self.assertEquals(response.status_code, 200)

    def test_can_add_photo(self):
        """Test if can insert photo."""
        count = ImagerProfile.objects.first().photos.count()
        with open('imager_images/static/default.jpeg', 'rb') as img:
            photo = SimpleUploadedFile('img.jpeg', img.read())
            data = {
                'title': 'for_test',
                'description': 'testing',
                'published': 'PRIVATE',
                'photo': photo
            }
            self.client.post(
                reverse_lazy('add_photo'),
                data,
                follow=True
            )
        self.assertEqual(ImagerProfile.objects.first().photos.count(), count + 1)

    def test_can_add_album(self):
        """Test if can insert photo."""
        count = ImagerProfile.objects.first().albums.count()
        with open('imager_images/static/default.jpeg', 'rb') as img:
            photo = SimpleUploadedFile('img.jpeg', img.read())
            data = {
                'title': 'for_test',
                'description': 'testing',
                'published': 'PRIVATE',
                'cover_photo': photo
            }
            self.client.post(
                reverse_lazy('add_album'),
                data,
                follow=True
            )
        self.assertEqual(ImagerProfile.objects.first().albums.count(), count)

    def test_can_access_album_edit_view(self):
        """Test all album edit viewe is accessible."""
        album_id = Album.objects.last().id
        response = self.client.get(reverse_lazy('edit_album', kwargs={'pk': album_id}))
        self.assertEquals(response.status_code, 200)

    def test_can_access_photo_edit_view(self):
        """Test all photo edit viewe is accessible."""
        photo_id = Photo.objects.last().id
        response = self.client.get(reverse_lazy('edit_photo', kwargs={'pk': photo_id}))
        self.assertEquals(response.status_code, 200)

    def test_can_edit_photo(self):
        """Test if can edit an existing photo."""
        photo_id = Photo.objects.last().id
        data = {
            'title': 'I\'ve changed it',
            'description': 'changed content',
            'published': 'PUBLIC',
        }
        self.client.post(
            reverse_lazy('edit_photo', kwargs={'pk': photo_id}),
            data,
            follow=True
        )
        self.assertEqual(ImagerProfile.objects.first().photos.last().title, 'I\'ve changed it')
        self.assertEqual(Photo.objects.last().title, 'I\'ve changed it')
        self.assertEqual(Photo.objects.last().description, 'changed content')
        self.assertEqual(Photo.objects.last().published, 'PUBLIC')

    def test_can_edit_album(self):
        """Test if can edit an existing album."""
        album_id = Album.objects.last().id
        with open('imager_images/static/default.jpeg', 'rb') as img:
            photo = SimpleUploadedFile('img.jpeg', img.read())
            data = {
                'title': 'I\'ve changed it',
                'description': 'changed content',
                'published': 'PUBLIC',
                'cover_photo': photo,
                'photo': photo
            }
            self.client.post(
                reverse_lazy('edit_album', kwargs={'pk': album_id}),
                data,
                follow=True
            )
        self.assertEqual(Album.objects.last().title, 'I\'ve changed it')
        self.assertEqual(Album.objects.last().description, 'changed content')
        self.assertEqual(Album.objects.last().published, 'PUBLIC')







