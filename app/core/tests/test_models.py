from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):
    def test_create_user_with_email_success(self):
        """Test creating a new user with an email is successful."""
        email = "test@gmail.com"
        password = "testpassword"
        user = get_user_model().objects.create_user(
            email = email,
            password = password
        )

        self.assertEqual(user.email,email)
        self.assertTrue(user.check_password(password))
    def test_new_user_email_normalized(self):
        """Test the email for a new user to be normalizd"""
        email = "test@GMAIL.COM"
        user = get_user_model().objects.create_user(email, 'testpassword')
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test that ensures that the email should be valid"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "testpassword")

    def test_create_super_user(self):
        """Creating a super user"""
        user =get_user_model().objects.create_superuser("test@gmail.com", 'testpassword')

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
