"""URL Configuration for Chronosphere DRF API

This module defines URL patterns for the Chronosphere DRF API.
It includes routes for:
- Rendering the index page
- Admin panel
- Authentication and authorization endpoints using Django Rest Framework
- User logout endpoint
- User registration and authentication endpoints using dj-rest-auth
- Profiles, posts, comments, likes, and followers endpoints

Additionally, it includes a handler for 404 errors, rendering the index page.

For more information, please refer to the Django documentation:
https://docs.djangoproject.com/en/3.2/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from .views import logout_route

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html')),
    path('admin/', admin.site.urls),
    path('api/api-auth/', include('rest_framework.urls')),
    path('api/dj-rest-auth/logout/', logout_route),
    path('api/dj-rest-auth/', include('dj_rest_auth.urls')),
    path(
        'api/dj-rest-auth/registration/', include(
            'dj_rest_auth.registration.urls')
    ),
    path('api/', include('profiles.urls')),
    path('api/', include('posts.urls')),
    path('api/', include('comments.urls')),
    path('api/', include('likes.urls')),
    path('api/', include('followers.urls')),
]

handler404 = TemplateView.as_view(template_name='index.html')
