from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from .models import Post
# Create your tests here.

class BlogTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = 'test',
            email = 'test@mail.com',
            password = 'testpass'
        )
        self.post = Post.objects.create(
            title = 'generic test title',
            body = 'test post body',
            author = self.user,
        )

    def test_string_representation(self):
        post = Post(title='generic test title')
        self.assertEqual(str(post), post.title)
    
    def test_post_content(self):
        self.assertEqual(f'{self.post.title}', 'generic test title')
        self.assertEqual(f'{self.post.author}', 'test')
        self.assertEqual(f'{self.post.body}', 'test post body')

    def test_list_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'test post body')
        self.assertTemplateUsed(response, 'index.html')

    def test_detail_view(self):
        response = self.client.get('/post/1/')
        no_response = self.client.get('/post/100/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'test post body')
        self.assertTemplateUsed(response, 'post_detail.html')


