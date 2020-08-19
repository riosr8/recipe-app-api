from django.test import TestCase
from django.contrib.auth import get_user_model
from core import models


def sample_user(email='test@test.com', password='password'):
    """Create a sample user"""
    return get_user_model().objects.create_user(
        email=email,
        password=password
    )


class ModelTests(TestCase):

    def test_create_user_with_email(self):
        """Test creating a new user with an email and password"""
        email = 'test@gmail.com'
        password = 'password123'

        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertEqual(user.check_password(password), True)

    def test_create_user_with_email_normalized(self):
        """Test the email for a new user is normalized"""
        email = 'test@GMAIL.COM'

        user = get_user_model().objects.create_user(
            email=email,
            password='password'
        )

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating a user with no email raises an error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'password')

    def test_create_new_superuser(self):
        """Test creating new superuser"""
        user = get_user_model().objects.create_superuser(
            'superuser@gmail.com',
            'superuser'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_tag_str(self):
        """Test the tag representation"""
        tag = models.Tag.objects.create(
            user=sample_user(),
            name='Test'
        )

        self.assertEqual(str(tag), tag.name)

    def test_ingredient_str(self):
        """Test the ingredient representation"""
        ingredient = models.Ingredient.objects.create(
            user=sample_user(),
            name='cucumber'
        )

        self.assertEqual(str(ingredient), ingredient.name)
