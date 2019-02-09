from rest_framework.generics import ListAPIView
from rest_framework import permissions
from posts.models import Post
from posts.api.serializers import PostModelSerializer
from django.db.models import Q
from .pagination import StandardResultsPagination

class UserPostListAPIView(ListAPIView):
    serializer_class = PostModelSerializer
    pagination_class = StandardResultsPagination

    def get_queryset(self, *args, **kwargs):
        qs = Post.objects.filter(user__username=self.kwargs['slug']).order_by("-updated_on")
        print(self.request.GET)
        query =self.request.GET.get("q",None)
        if query is not None:
            qs=qs.filter(
                Q(content__icontains=query) |
                Q(user__username__icontains=query)
            )
        return qs