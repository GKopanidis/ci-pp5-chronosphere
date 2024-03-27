from django.contrib import admin
from .models import Like

# Register your models here.


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Like model.
    """
    list_display = ['owner', 'post', 'created_at']
    search_fields = ['owner__username', 'post__title']
    list_filter = ['created_at']
