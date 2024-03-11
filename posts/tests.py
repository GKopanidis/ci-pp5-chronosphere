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


class PostDetailViewTests(APITestCase):
    def setUp(self):
        spartan = User.objects.create_user(
            username='spartan', password='password')
        chaos = User.objects.create_user(username='chaos', password='password')
        Post.objects.create(
            owner=spartan, title='Test Post', content='Test Content'
        )
        Post.objects.create(
            owner=chaos, title='Test Post 2', content='Test Content 2'
        )

    def test_can_retrieve_post_using_valid_id(self):
        response = self.client.get('/posts/1/')
        self.assertEqual(response.data['title'], 'Test Post')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cannot_retrieve_post_using_invalid_id(self):
        response = self.client.get('/posts/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_logged_in_user_can_update_own_post(self):
        self.client.login(username='spartan', password='password')
        response = self.client.put('/posts/1/', {'title': 'Updated Post'})
        post = Post.objects.filter(pk=1).first()
        self.assertEqual(post.title, 'Updated Post')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_in_user_cannot_update_other_user_post(self):
        self.client.login(username='spartan', password='password')
        response = self.client.put('/posts/2/', {'title': 'Updated Post'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
