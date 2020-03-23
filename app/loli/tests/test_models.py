from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    
    def test_create_user_with_email_successful(self):
        '''Testing creating a new user with an email is sucessfull '''
        # username = 'romjan1412'
        email = 'romjanhossain726526@gmail.com'
        password = 'whoCares1234'
        user = get_user_model().objects.create_user(email=email,password=password)

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
