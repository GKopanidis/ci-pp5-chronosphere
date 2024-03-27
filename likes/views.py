from rest_framework import generics, permissions
from chronosphere_drf_api.permissions import IsOwnerOrReadOnly
from likes.models import Like
from likes.serializers import LikeSerializer

# Create your views here.


class LikeList(generics.ListCreateAPIView):
    """
    View for listing and creating like instances.

    Attributes:
        permission_classes (list): A list of permission classes controlling
        access to the view.
        serializer_class: The serializer class used for serializing and
        deserializing likes.
        queryset: The queryset of likes used in the view.

    Methods:
        perform_create: Method called during like creation to set the owner.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = LikeSerializer
    queryset = Like.objects.all()

    def perform_create(self, serializer):
        """
        Method called during like creation.

        Args:
            serializer: The serializer instance used for creating the like.

        Behavior:
            Sets the owner of the like to the request user.
        """
        serializer.save(owner=self.request.user)


class LikeDetail(generics.RetrieveDestroyAPIView):
    """
    View for retrieving and deleting individual like instances.

    Attributes:
        permission_classes (list): A list of permission classes controlling
        access to the view.
        serializer_class: The serializer class used for serializing and
        deserializing likes.
        queryset: The queryset of likes used in the view.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = LikeSerializer
    queryset = Like.objects.all()
