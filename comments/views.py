from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from chronosphere_drf_api.permissions import IsOwnerOrReadOnly
from .models import Comment
from .serializers import CommentSerializer, CommentDetailSerializer


# Create your views here.


class CommentList(generics.ListCreateAPIView):
    """
    A view for listing and creating comments.

    Attributes:
        permission_classes (list): A list of permission classes controlling
        access to the view.
        serializer_class: The serializer class used for serializing and
        deserializing comments.
        queryset: The queryset of comments used in the view.
        filter_backends (list): A list of backend classes used for filtering
        comments.
        filterset_fields (list): A list of fields by which comments can be
        filtered.

    Methods:
        perform_create: Method called during comment creation to set the owner
        and parent if applicable.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['post', 'parent']

    def perform_create(self, serializer):
        """
        Create method called during comment creation.

        Args:
            serializer: The serializer instance used for creating the comment.

        Behavior:
            Checks if the comment has a parent, and sets the owner and parent
            if applicable.
        """
        parent_id = self.request.data.get('parent')
        if parent_id is not None:
            parent = Comment.objects.get(id=parent_id)
            serializer.save(owner=self.request.user, parent=parent)
        else:
            serializer.save(owner=self.request.user)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    A view for retrieving, updating, and deleting individual comments.

    Attributes:
        permission_classes (list): A list of permission classes controlling
        access to the view.
        serializer_class: The serializer class used for serializing and
        deserializing detailed comment information.
        queryset: The queryset of comments used in the view.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = CommentDetailSerializer
    queryset = Comment.objects.all()
