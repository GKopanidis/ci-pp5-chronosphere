from django.contrib import admin
from .models import Post, Category

# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'owner', 'created_at', 'updated_at', 'category']
    search_fields = ['title', 'owner__username', 'category__name']
    list_filter = ['created_at', 'updated_at', 'category']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
