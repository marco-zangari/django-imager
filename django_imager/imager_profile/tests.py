"""Test for django-imager apps."""
from django.test import TestCase

# Create your tests here.

from imager_profile.models import User
import factory
from django.test import Client


class UserFactory(factory.django.DjangoModelFactory):
    """Factory boy!"""
    class Meta:
        model = User


class ProfileTests(TestCase):
    """Testing for the imager_profile app/model."""

    def setUp(self):
        """Initiate with two users in the db, one activce and one not."""
        user = UserFactory.build()
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

        user = UserFactory.build()
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


class ViewTest(TestCase):
    """Testing for the imager_profile app/model."""

    def setUp(self):
        """Initiate with two users in the db, one activce and one not."""
        user = UserFactory.build()
        user.username = 'john'
        user.email = 'john@image.com'
        user.set_password('password')
        user.save()
        self.client = Client()

    def test_can_access_main_view(self):
        """Test home view is accessible."""
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_can_access_login_view(self):
        """Test login view is accessible."""
        response = self.client.get('/login')
        self.assertEquals(response.status_code, 200)

    def test_can_access_logout_view(self):
        """Test logout view is accessible."""
        response = self.client.get('/logout')
        self.assertEquals(response.status_code, 200)

    def test_user_can_login_successful(self):
        """Test if we can login successful."""
        response = self.client.post('/login', {'username': 'john', 'password': 'password'}, follow=True)
        self.assertEquals(response.status_code, 200)
        # import pdb; pdb.set_trace()
        self.assertIn(b'Welcome to Home Page home', response.content)
