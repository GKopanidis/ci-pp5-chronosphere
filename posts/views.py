from django.db.models import Count
from rest_framework import generics, permissions, filters
from rest_framework.views import APIView
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from chronosphere_drf_api.permissions import IsOwnerOrReadOnly
from .models import Post, Category
from .serializers import PostSerializer, CategorySerializer

# Create your views here.


class CategoryList(generics.ListAPIView):
    """
    View for listing categories.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TopCategoriesList(APIView):
    """
    View for listing top categories.
    """
    def get(self, request, format=None):
        """
        Method to handle GET requests for top categories.

        Args:
            request: The request object.
            format: The format of the response data.

        Returns:
            Response: Response object containing top categories data.
        """
        categories = Category.objects.annotate(
            num_posts=Count('posts')
        ).order_by('-num_posts')[:5]
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)


class PostList(generics.ListCreateAPIView):
    """
    View for listing and creating posts.
    """
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.annotate(
        likes_count=Count('likes', distinct=True),
        comments_count=Count('comment', distinct=True)
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'owner__followed__owner__profile',
        'likes__owner__profile',
        'owner__profile',
        'category',
    ]
    search_fields = [
        'owner__username',
        'title',
    ]
    ordering_fields = [
        'likes_count',
        'comments_count',
        'likes__created_at',
    ]

    def perform_create(self, serializer):
        """
        Method to perform creation of a new post.

        Args:
            serializer: The serializer instance.

        Returns:
            None
        """
        serializer.save(owner=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    View for retrieving, updating and deleting posts.
    """
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Post.objects.annotate(
        likes_count=Count('likes', distinct=True),
        comments_count=Count('comment', distinct=True)
    ).order_by('-created_at')
