from django.urls import path
from posts import views
from .views import CategoryList, TopCategoriesList

urlpatterns = [
    path('posts/', views.PostList.as_view()),
    path('posts/<int:pk>/', views.PostDetail.as_view()),
    path('categories/', CategoryList.as_view(), name='category-list'),
    path('top-categories/', TopCategoriesList.as_view(), name='top-categories'),
]
