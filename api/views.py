from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from api.serializers import PostSerializer
from api.permissions import IsAuthorOrReadOnly
from posts.models import Post


class PostListCreateAPIView(generics.ListCreateAPIView):
    """Postlarni ko'rish va yangi post yaratish."""
    
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def perform_create(self, serializer):
        """Yangi post yaratishda muallifni avtomatik belgilash."""
        serializer.save(author=self.request.user)


class PostRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """Postni ko'rish, tahrirlash va o'chirish."""
    
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrReadOnly]