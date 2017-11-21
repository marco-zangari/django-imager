"""Test for django-imager apps."""
from django.test import TestCase

# Create your tests here.

from models import ImagerProfile, User


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


def test_user_has_username(self):
    """."""
