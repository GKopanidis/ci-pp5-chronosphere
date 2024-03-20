from django.urls import path
from profiles import views
from .views import UserTopCategories

urlpatterns = [
    path('profiles/', views.ProfileList.as_view()),
    path('profiles/<int:pk>/', views.ProfileDetail.as_view()),
    path('user-top-categories/', UserTopCategories.as_view(),
         name='user-top-categories'),
]
