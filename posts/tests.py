from django.contrib.auth.models import User
from .models import Post
from rest_framework import status
from rest_framework.test import APITestCase


class PostListViewTests(APITestCase):
    """
    Test cases for the Post List View.
    """

    def setUp(self):
        """
        Set up the test data.
        """
        User.objects.create_user(username='spartan', password='password')

    def test_can_list_posts(self):
        """
        Test if posts can be listed.
        """
        spartan = User.objects.get(username='spartan')
        Post.objects.create(owner=spartan, title='Test Post')
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_logged_in_user_can_create_post(self):
        """
        Test if a logged-in user can create a post.
        """
        self.client.login(username='spartan', password='password')
        response = self.client.post('/posts/', {'title': 'Test Post'})
        count = Post.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_not_logged_in_cannot_create_post(self):
        """
        Test if a user not logged in cannot create a post.
        """
        response = self.client.post('/posts/', {'title': 'Test Post'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class PostDetailViewTests(APITestCase):
    """
    Test cases for the Post Detail View.
    """

    def setUp(self):
        """
        Set up the test data.
        """
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
        """
        Test if a post can be retrieved using a valid ID.
        """
        response = self.client.get('/posts/1/')
        self.assertEqual(response.data['title'], 'Test Post')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cannot_retrieve_post_using_invalid_id(self):
        """
        Test if a post cannot be retrieved using an invalid ID.
        """
        response = self.client.get('/posts/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_logged_in_user_can_update_own_post(self):
        """
        Test if a logged-in user can update their own post.
        """
        self.client.login(username='spartan', password='password')
        response = self.client.put('/posts/1/', {'title': 'Updated Post'})
        post = Post.objects.filter(pk=1).first()
        self.assertEqual(post.title, 'Updated Post')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_in_user_cannot_update_other_user_post(self):
        """
        Test if a logged-in user cannot update another user's post.
        """
        self.client.login(username='spartan', password='password')
        response = self.client.put('/posts/2/', {'title': 'Updated Post'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_logged_in_user_can_delete_own_post(self):
        """
        Test if a logged-in user can delete their own post.
        """
        self.client.login(username='spartan', password='password')
        response = self.client.delete('/posts/1/')
        count = Post.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_logged_in_user_cannot_delete_other_user_post(self):
        """
        Test if a logged-in user cannot delete another user's post.
        """
        self.client.login(username='spartan', password='password')
        response = self.client.delete('/posts/2/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_not_logged_in_cannot_delete_post(self):
        """
        Test if a user not logged in cannot delete a post.
        """
        response = self.client.delete('/posts/1/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
