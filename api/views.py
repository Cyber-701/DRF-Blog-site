from django.shortcuts import render
from api.serializers import PostSerializer
from posts.models import Post
from rest_framework.views import APIView, Response
from rest_framework import generics

# Create your views here.
# class PostListView(APIView):
#     def get(self, request):
#         posts = Post.objects.all()
#         serializers = PostSerializer(posts, many=True)
#         return Response(serializers.data)

# class PostListAPIView(generics.ListAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


# class PostCreateAPIView(generics.CreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
    
class PostListCreateAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDeleteUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
    """Update va Delete bitta clasda"""
    queryset = Post.objects.all()
    serializer_class = PostSerializer   