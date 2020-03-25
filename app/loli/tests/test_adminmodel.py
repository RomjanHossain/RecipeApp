from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@gmail.com',
            password='whoCares,1232'
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='whocares@email.com',
            password='N-word5',
            name='User Name'
        )

    def test_user_listed(self):
        """ Test that user are listed or not """
        url = reverse('admin:core_user_changelist')
        response = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)