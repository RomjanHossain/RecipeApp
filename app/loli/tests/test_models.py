from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def creating_super_user(self):
        """ Creating super user test """
        email, password = 'romjanhosaain@gmil.com', 'holyshit2323'
        user = get_user_model().objects.create_superuser(email=email, password=password)

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_create_user_with_email_successful(self):
        '''Testing creating a new user with an email is sucessfull '''
        # username = 'romjan1412'
        email = 'romjanhossain726526@gmail.com'
        password = 'whoCares1234'
        user = get_user_model().objects.create_user(email=email, password=password)

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_usermodel(self):
        """testing if user email is normalize """
        email = "romjanhossain@GMAILfuFKJ.Com"
        user = get_user_model().objects.create_user(email, 'hello1312')
        # print(f'This is user email = {user.email}')
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')
    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'test@londonappdev.com',
            'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
