from django.contrib.auth.models import User
from .models import Post
from rest_framework import status
from rest_framework.test import APITestCase

# Create your tests here.


class PostListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='spartan', password='password')

    def test_can_list_posts(self):
        spartan = User.objects.get(username='spartan')
        Post.objects.create(owner=spartan, title='Test Post')
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        print(len(response.data))

    def test_logged_in_user_can_create_post(self):
        self.client.login(username='spartan', password='password')
        response = self.client.post('/posts/', {'title': 'Test Post'})
        count = Post.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_not_logged_in_cannot_create_post(self):
        response = self.client.post('/posts/', {'title': 'Test Post'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
