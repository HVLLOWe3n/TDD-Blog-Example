from django.test import TestCase
from django.contrib.auth.models import User
from django.test.client import Client
from django.urls import reverse


class AccountTest(TestCase):
    def setUp(self):
        self.c = Client()

    # When Mark wants to register
    def test_when_user_wants_to_sign_up(self):
        user_data = {
            'first_name': 'Mark',
            'last_name': 'Zuckerberg',
            'username': 'Zuck',
            'email': 'Zuck@gmail.com',
            'password': 'MySimplePassword',
        }

        response = self.c.post(reverse('sign_up'), data=user_data)
        mark = User.objects.get(username=user_data['username'])

        self.assertEqual(response.status_code, 200)
        self.assertEqual(user_data['username'], mark.username)
        # self.assertTrue(request.user.is_authenticated())

    # When Mark wants to log in
    def test_when_user_wont_to_sign_in(self):
        user_data = {
            'username': 'Zuck',
            'password': 'MySimplePassword',
        }

        response = self.c.post(reverse('sign_in'), data=user_data)

        self.assertTrue(response.status_code, 200)
