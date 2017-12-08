"""Test for django-imager apps."""
from django.test import TestCase

# Create your tests here.

from imager_profile.models import User
import factory
from django.test import Client
from django.urls import reverse_lazy


class UserFactory(factory.django.DjangoModelFactory):
    """Factory boy!"""
    class Meta:
        model = User


class ViewTest(TestCase):
    """Testing for the imagersite app/model."""

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

    def test_user_can_login_successful(self):
        """Test if we can login successful."""
        response = self.client.post('/login', {'username': 'john', 'password': 'password'}, follow=True)
        self.assertEquals(response.status_code, 200)
        # import pdb; pdb.set_trace()
        self.assertIn(b'Welcome to Home Page home', response.content)
        response = self.client.get('/logout', follow=True)
        self.assertEquals(response.status_code, 200)

    def test_register_view_status_code_200(self):
        """Test register view has 200 status."""
        response = self.client.get(reverse_lazy('registration_register'))
        self.assertEqual(response.status_code, 200)

    def test_newly_registered_user_exists_and_is_inactive(self):
        """Test new user is inactive."""
        data = {
            'username': 'linda',
            'password1': 'phtato12345_abc',
            'password2': 'phtato12345_abc',
            'email': 'linda@1234.com'
        }
        self.client.post(
            reverse_lazy('registration_register'),
            data,
            follow=True
        )
        self.assertFalse(User.objects.all()[1].is_active)
