from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from comments.models import Comment
from comments.api.serializers import CommentSerializer
from comments.api.permissions import IsOwnerOrReadAndCreatedOnly

class CommentApiViewSet(ModelViewSet):
    permission_classes = [IsOwnerOrReadAndCreatedOnly]
    
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    
    # ordena el listado de comentarios utilizando el sistema de filtros del rest_framework
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    ordering = ['-created_at']
    
    # filtra los comentarios por el campo post
    filterset_fields = ['post']
    