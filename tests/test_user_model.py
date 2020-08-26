from django.test import TestCase
from django.contrib.auth import get_user_model
from django.db.utils import IntegrityError

User = get_user_model()


class UserModelTest(TestCase):
    def test_create_user_without_names_successfully(self):
        user = User.objects.create_user(
            email="example@gmail.com",
            password="passw0rd1"
        )
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_admin)
        self.assertEqual(user.email, "example@gmail.com")

    def test_create_user_with_names_successfully(self):
        user = User.objects.create_user(
            email="example@gmail.com",
            password="passw0rd1",
            first_name="Test",
            last_name="User"
        )
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_admin)
        self.assertEqual(user.email, "example@gmail.com")
        self.assertEqual(user.first_name, "Test")
        self.assertEqual(user.last_name, "User")

    def test_create_duplicate_user_fail(self):
        User.objects.create_user(
            email="example@gmail.com",
            password="passw0rd1"
        )
        with self.assertRaises(IntegrityError):
            User.objects.create_user(
                email="example@gmail.com",
                password="passw0rd1"
            )
