from rest_framework.viewsets import ModelViewSet

from comments.models import Comment
from comments.api.serializers import CommentSerializer


class CommentApiViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    