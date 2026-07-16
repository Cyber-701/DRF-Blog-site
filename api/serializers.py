# In api/serializers.py
from rest_framework import serializers
from posts.models import Post
from django.contrib.auth import get_user_model


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """User ma'lumotlarini serializatsiya qilish."""
    
    class Meta:
        model = User
        fields = ["username", "email"]
        read_only_fields = ["username"]


class PostSerializer(serializers.ModelSerializer):
    """Post ma'lumotlarini serializatsiya qilish."""
    
    author = UserSerializer(read_only=True)
    author_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        source="author",
        write_only=True,
        required=False
    )
    
    class Meta:
        model = Post
        fields = ["id", "author", "author_id", "title", "body", "created", "updated"]
        read_only_fields = ["created", "updated"]