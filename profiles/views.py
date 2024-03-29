from django.db.models import Count
from rest_framework import generics, filters
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from chronosphere_drf_api.permissions import IsOwnerOrReadOnly
from .models import Profile
from posts.models import Post
from .serializers import ProfileSerializer

# Create your views here.


class ProfileList(generics.ListAPIView):
    """
    API endpoint for listing profiles.

    Retrieves a list of profiles with annotated counts for posts, followers,
    and following.

    Supports filtering and ordering by various fields.

    Args:
        generics.ListAPIView: ListAPIView subclass for listing profiles.

    Returns:
        Response: A response containing serialized profile data.
    """
    queryset = Profile.objects.annotate(
        posts_count=Count('owner__post', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True)
    ).order_by('-created_at')
    serializer_class = ProfileSerializer
    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'owner__followed__owner__profile',
    ]
    ordering_fields = [
        'posts_count',
        'followers_count',
        'following_count',
        'owner__following__created_at',
        'owner__followed__created_at',
    ]


class ProfileDetail(generics.RetrieveUpdateAPIView):
    """
    API endpoint for retrieving and updating a profile.

    Retrieves details of a specific profile and allows updates if the request
    user is the owner.

    Args:
        generics.RetrieveUpdateAPIView: RetrieveUpdateAPIView subclass for
        retrieving and updating profiles.

    Returns:
        Response: A response containing serialized profile data.
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.annotate(
        posts_count=Count('owner__post', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True)
    ).order_by('-created_at')
    serializer_class = ProfileSerializer


class UserTopCategories(APIView):
    """
    API endpoint for retrieving a user's top categories.

    Retrieves the top categories of posts created by the request user.

    Args:
        APIView: APIView subclass for handling HTTP GET requests.

    Returns:
        Response: A response containing the top categories data.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user_posts = Post.objects.filter(owner=request.user)
        top_categories = (
            user_posts
            .values('category__name', 'category__id')
            .annotate(total=Count('id'))
            .order_by('-total')[:5]
        )
        return Response(top_categories)
