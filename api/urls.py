from django.urls import path
from .views import PostListCreateAPIView, PostDeleteUpdateAPIView#PostListAPIView, PostCreateAPIView

app_name = "api"
urlpatterns = [
    path('', PostListCreateAPIView.as_view(), name='list-create'),
    path('<int:pk>/', PostDeleteUpdateAPIView.as_view(), name="Update-Delete")
#    path('', PostListAPIView.as_view(), name='list'),
#    path('create/',PostCreateAPIView.as_view(), name= 'create'),
]