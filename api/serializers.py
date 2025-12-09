# In api/serializers.py
from rest_framework.serializers import ModelSerializer
from posts.models import Post

class PostSerializer(ModelSerializer):  # Changed from PostSerializers to PostSerializer
    class Meta:
        model = Post
        fields = ["id", "author", "title", "body", "created", "updated"]