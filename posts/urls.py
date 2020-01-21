from django.urls import path
from .views import PostsList , PostsDetail

urlpatterns = [
    path('post/', PostsList.as_view(), name='posts_list'),
    path('post/<int:pk>/', PostsDetail.as_view(), name='posts_detail'),
]