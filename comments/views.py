from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from chronosphere_drf_api.permissions import IsOwnerOrReadOnly
from .models import Comment
from .serializers import CommentSerializer, CommentDetailSerializer


# Create your views here.


class CommentList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['post', 'parent']

    def perform_create(self, serializer):
        parent_id = self.request.data.get('parent')
        if parent_id is not None:
            parent = Comment.objects.get(id=parent_id)
            serializer.save(owner=self.request.user, parent=parent)
        else:
            serializer.save(owner=self.request.user)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = CommentDetailSerializer
    queryset = Comment.objects.all()
