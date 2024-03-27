from django.apps import AppConfig


class PostsConfig(AppConfig):
    """
    AppConfig for the posts app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'posts'
