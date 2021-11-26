from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from categories.models import Category
from categories.api.serializers import CategorySerializer
from categories.api.permissions import IsAdminOrReadOnly


class CategoryApiViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    
    serializer_class = CategorySerializer
    # queryset = Category.objects.all()
    queryset = Category.objects.filter(published=True)

    # cambia el índice de búsqueda de ID a Slug
    lookup_field = 'slug'
    
    # filtros
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title']