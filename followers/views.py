from rest_framework import generics, permissions
from chronosphere_drf_api.permissions import IsOwnerOrReadOnly
from .models import Follower
from .serializers import FollowerSerializer

# Create your views here.


class FollowerList(generics.ListCreateAPIView):
    """
    View for listing and creating follower instances.

    Attributes:
        permission_classes (list): A list of permission classes controlling
        access to the view.
        queryset: The queryset of followers used in the view.
        serializer_class: The serializer class used for serializing and
        deserializing followers.

    Methods:
        perform_create: Method called during follower creation to set the
        owner.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer

    def perform_create(self, serializer):
        """
        Method called during follower creation.

        Args:
            serializer: The serializer instance used for creating the follower.

        Behavior:
            Sets the owner of the follower to the request user.
        """
        serializer.save(owner=self.request.user)


class FollowerDetail(generics.RetrieveDestroyAPIView):
    """
    View for retrieving and deleting individual follower instances.

    Attributes:
        permission_classes (list): A list of permission classes controlling
        access to the view.
        queryset: The queryset of followers used in the view.
        serializer_class: The serializer class used for serializing and
        deserializing followers.
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer
