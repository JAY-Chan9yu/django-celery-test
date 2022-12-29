from rest_framework import mixins, viewsets
from rest_framework.response import Response

from apps.posts.models import Post
from apps.posts.serializers import PostSerializer
from apps.posts.sqs_tasks import send_post_read_alert_sqs
from apps.posts.tasks import send_post_read_alert


class PostViewSet(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  viewsets.GenericViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        # sqs
        send_post_read_alert_sqs.delay(1)
        # rabbit
        send_post_read_alert.delay(1)
        return Response(serializer.data)
