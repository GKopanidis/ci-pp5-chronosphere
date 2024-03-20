from django.contrib import admin
from .models import Follower

# Register your models here.


@admin.register(Follower)
class FollowerAdmin(admin.ModelAdmin):
    list_display = ['owner', 'followed', 'created_at']
    search_fields = ['owner__username', 'followed__username']
    list_filter = ['created_at']
