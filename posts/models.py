from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    """
    Model representing a category for posts.
    """
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        """
        String representation of the category object.

        Returns:
            str: The name of the category.
        """
        return self.name

    class Meta:
        ordering = ['name']


class Post(models.Model):
    """
    Model representing a post.
    """
    image_filter_choices = [
        ('_1977', '1977'),
        ('brannan', 'Brannan'),
        ('earlybird', 'Earlybird'),
        ('hudson', 'Hudson'),
        ('inkwell', 'Inkwell'),
        ('lofi', 'Lo-Fi'),
        ('kelvin', 'Kelvin'),
        ('normal', 'Normal'),
        ('nashville', 'Nashville'),
        ('rise', 'Rise'),
        ('toaster', 'Toaster'),
        ('valencia', 'Valencia'),
        ('walden', 'Walden'),
        ('xpro2', 'X-pro II')
    ]
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_post_ulmn61', blank=True
    )
    image_filter = models.CharField(
        max_length=32, choices=image_filter_choices, default='normal'
    )
    category = models.ForeignKey(
        Category, related_name='posts', on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        """
        String representation of the post object.

        Returns:
            str: A string containing the ID and title of the post.
        """
        return f'{self.id} {self.title}'
