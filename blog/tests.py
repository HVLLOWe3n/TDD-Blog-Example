from django.test import TestCase
from django.test.client import Client
from django.urls import reverse

from datetime import datetime

from .models import Post


# 1. user story
# 2. expected fail
# 3. write minimum code needed for test(s) to pass


class TestMainPage(TestCase):

    def setUp(self):
        self.c = Client()

    # When a Mark go to url ('/') 200 code status back
    def test_go_to_root_url_main_page_view(self):
        response = self.c.get(reverse('post_list'))         # Get object request

        self.assertEqual(response.status_code, 200)         # equal

    # When a Mark visits a page, display 'Hello world'
    def test_user_go_to_root_url(self):
        response = self.c.get(reverse('post_list'))

        get_html_text = response.content.decode('utf8')

        self.assertIn('<title>Main Page</title>', get_html_text)


class TestPostWithDataBase(TestCase):
    def setUp(self):
        Post.objects.create(author='Roman', title='Title', text='Text')
        Post.objects.create(author='Alex', title='Title 1', text='Text 1')

    # Когда Марк добавил пост, проверяем успешно ли он к нам пришел
    def test_add_new_post_to_data_base(self):
        new_mail = {
            'author': 'Roman',
            'title': 'Some Title',
            'text': 'Some Text',
            'date': datetime.now(),
            'publish_date': datetime.now(),
        }

        self.client.post(reverse('new_mail_post'), data=new_mail)

        self.assertTrue(Post.objects.filter(id=3).exists(), True)

    # Когда марк заходит по URL('/post/1/') он видит страницу с определенным постом
    def test_when_user_wont_open_post_detail(self):
        response = self.client.get(reverse('post_detail', kwargs={'pk': 1}))

        get_text_html = response.content.decode('utf8')

        self.assertIn(Post.objects.filter(author='Roman').first().title, get_text_html)
        self.assertIn(Post.objects.filter(author='Roman').first().author, get_text_html)
        self.assertIn(Post.objects.filter(author='Roman').first().text, get_text_html)

    # Когда Марк переходит по URL('post/list') он видит страницу со всеми постами
    def test_when_user_go_to_post_list(self):
        response = self.client.get(reverse('post_list'))

        get_text_html = response.content.decode('utf8')
        id_list = Post.objects.values_list('id', flat=True)

        for id in id_list:
            self.assertIn(Post.objects.filter(id=id).first().title, get_text_html)
            self.assertIn(Post.objects.filter(id=id).first().author, get_text_html)
            self.assertIn(Post.objects.filter(id=id).first().text, get_text_html)

# orm notes for roman:
# object = model(param='x', param='x')
# object.save()

# or create()
