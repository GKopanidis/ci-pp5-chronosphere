from django.contrib import admin
from .models import Comment


# Register your models here.

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['content', 'owner', 'post', 'created_at', 'updated_at']
    search_fields = ['content', 'owner__username', 'post__title']
    list_filter = ['created_at', 'updated_at']
