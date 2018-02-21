from django.test import TestCase
from django.test.client import Client
from django.urls import reverse

from .models import Post


# 1. user story
# 2. expected fail
# 3. write minimum code needed for test(s) to pass


class TestMainPage(TestCase):

    def setUp(self):
        self.c = Client()

    # When a Mark go to url ('/') 200 code status back
    def test_go_to_root_url_main_page_view(self):
        response = self.c.get(reverse('main_page'))         # Get object request

        self.assertEqual(response.status_code, 200)         # equal

    # When a Mark visits a page, display 'Hello world'
    def test_user_go_to_root_url(self):
        response = self.c.get(reverse('main_page'))

        get_html_text = response.content.decode('utf8')

        self.assertIn('<title>Hello World</title>', get_html_text)


class TestPostsDataBase(TestCase):

    # Когда Марк добавил пост, проверяем успешно ли он к нам пришел
    def test_add_new_post_to_data_base(self):
        new_mail = {
            'author': 'Roman',
            'title': 'Some Title',
            'text': 'Some Text',
        }

        self.client.post(reverse('new_mail_post'), data=new_mail)

        self.assertEqual(new_mail['author'], Post.objects.filter(author='Roman').first().author)
# orm notes for roman:
# object = model(param='x', param='x')
# object.save()

# or create()