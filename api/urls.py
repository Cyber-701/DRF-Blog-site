from django.urls import path

from .views import PostListCreateAPIView, PostRetrieveUpdateDestroyAPIView


app_name = "api"

urlpatterns = [
    path('', PostListCreateAPIView.as_view(), name='list-create'),
    path('<int:pk>/', PostRetrieveUpdateDestroyAPIView.as_view(), name='detail-update-delete'),
]