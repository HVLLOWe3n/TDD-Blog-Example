from django.test import TestCase
from django.test.client import Client
from django.urls import reverse

# 1. user story
# 2. expected fail
# 3. write minimum code needed for test(s) to pass


class TestMainPage(TestCase):

    def setUp(self):
        self.c = Client()

    # when we go to url ('/') 200 code status back
    def test_go_to_root_url_main_page_view(self):
        response = self.c.get(reverse('main_page'))         # Get object request

        self.assertEqual(response.status_code, 200)         # equal

    # When a user visits a page, display 'Hello world'
    def test_user_go_to_root_url(self):
        response = self.c.get(reverse('main_page'))

        get_html_text = response.content.decode('utf8')

        self.assertIn('<title>Hello World</title>', get_html_text)
