from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Follower(models.Model):
    """
    Model representing a follower relationship between users.
    """
    owner = models.ForeignKey(
        User, related_name='following', on_delete=models.CASCADE
    )
    followed = models.ForeignKey(
        User, related_name='followed', on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'followed']

    def __str__(self):
        """
        String representation of the follower object.

        Returns:
            str: A string containing the owner and followed usernames.
        """
        return f'{self.owner} {self.followed}'
