from rest_framework import generics
from .models import Posts
from .serializers import PostsSerializer 
from .permissions import IsAuthorOrReadOnly

class PostsList(generics.ListCreateAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer
    permission_classes = (IsAuthorOrReadOnly,)


class PostsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer
