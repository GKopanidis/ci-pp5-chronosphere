from django.apps import AppConfig


class CommentsConfig(AppConfig):
    """
    AppConfig for the comments app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'comments'
