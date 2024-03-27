from django.db import models
from django.contrib.auth.models import User
from posts.models import Post

# Create your models here.


class Comment(models.Model):
    """
    Model representing a comment on a post.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='replies',
        verbose_name="Parent Comment"
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        """
        String representation of the comment object.

        Returns:
            str: The first 20 characters of the comment content.
        """
        return self.content[:20]
