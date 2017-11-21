"""Test for django-imager apps."""
from django.test import TestCase

# Create your tests here.

from imager_profile.models import ImagerProfile, User


class ProfileTests(TestCase):
    """Testing for the imager_profile app/model."""

    def setUp(self):
        """Initiate with two users in the db, one activce and one not."""
        user = User(username='john', email='john@image.com')
        user.set_password('password')
        user.save()
        profile = ImagerProfile(website='www.iphoto.com',
                                camera='Nikkon',
                                location='studio destiny',
                                bio='I take pictures',
                                phone='(000) 111 2222',
                                user=user)
        profile.save()

        user = User(username='nick', email='nick@image.com')
        user.set_password('password')
        user.save()
        profile = ImagerProfile(website='www.imgluv.com',
                                camera='Sony',
                                location='studio hell',
                                bio='I take pictures too',
                                phone='(000) 222 3333',
                                user=user)
        profile.save()

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
