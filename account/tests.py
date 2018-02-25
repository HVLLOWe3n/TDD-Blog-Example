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
            'firstname': 'Mark',
            'lastname': 'Zuckerberg',
            'username': 'Zuck',
            'email': 'Zuck@gmail.com',
            'password': 'MySimplePassword',
        }

        response = self.c.post(reverse('sign_up'), data=user_data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(user_data['email'], User.objects.get(email=user_data['email']).email)
