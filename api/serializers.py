# In api/serializers.py
from rest_framework.serializers import ModelSerializer
from posts.models import Post
from django.contrib.auth.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email"]

class PostSerializer(ModelSerializer):
#    author = UserSerializer()  # Changed from PostSerializers to PostSerializer
    class Meta:
        model = Post
        fields = ["id", "author", "title", "body", "created", "updated"]
#        depth = 1