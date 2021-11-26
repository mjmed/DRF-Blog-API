from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from posts.models import Post
from posts.api.serializers import PostSerializer
from posts.api.permissions import IsAdminOrReadOnly


class PostApiViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    
    serializer_class = PostSerializer
    queryset = Post.objects.filter(published=True)
    
    lookup_field = 'slug'
    
    filter_backends = [DjangoFilterBackend]
    # filtra por el id de la categoria
    # filterset_fields = ['category']
    
    # filtra por el slug de la categoria
    # filterset_fields = ['category__slug']
    
    # filtra por el id y por el slug de la categoria
    filterset_fields = ['category', 'category__slug']