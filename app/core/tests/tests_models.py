import email
from django.test import TestCase
from django.contrib.auth import get_user_model

class TestModel(TestCase):
    def test_create_user_with_email_success(self):
        email = 'aarya@gmail.com'
        password = 'Test123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email,email)
        self.assertTrue(user.check_password(password))

    def test_create_user_with_normalise_email(self):
        email = 'aaryas@GMAIL.COM'
        user= get_user_model().objects.create_user(email,'test123')

        self.assertEqual(user.email,email.lower())

    def test_new_user_invalid_email(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None,'tesr1')

    def test_create_new_superuser(self):
        user =get_user_model().objects.create_superuser('test@GMAIL.COM','test123')
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)


