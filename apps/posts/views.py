from rest_framework import mixins, viewsets

from apps.posts.models import Post
from apps.posts.serializers import PostSerializer


class PostViewSet(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  viewsets.GenericViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
