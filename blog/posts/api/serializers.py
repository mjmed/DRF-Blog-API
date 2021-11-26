from rest_framework import serializers

from posts.models import Post
from users.api.serializers import UserSerializer


class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    
    class Meta:
        model = Post
        fields = ['title', 'content', 'slug', 'miniature', 'created_at',
                  'published', 'user', 'category']