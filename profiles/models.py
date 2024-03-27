from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    """
    Model representing a user profile.
    """
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255, blank=True)
    content = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_profile_eyefzf'
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        """
        String representation of the profile object.

        Returns:
            str: A string containing the owner's username and 'profile'.
        """
        return f"{self.owner}'s profile"


def create_profile(sender, instance, created, **kwargs):
    """
    Signal handler to create a profile when a new user is created.

    Args:
        sender: The sender of the signal.
        instance: The instance of the sender.
        created: A boolean indicating if the instance was created.
        **kwargs: Additional keyword arguments.

    Returns:
        None
    """
    if created:
        Profile.objects.create(owner=instance)


post_save.connect(create_profile, sender=User)
