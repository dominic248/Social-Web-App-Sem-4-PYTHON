from rest_framework.generics import ListAPIView,CreateAPIView
from rest_framework import permissions
from ..models import Post
from .serializers import PostModelSerializer
from django.db.models import Q
from .pagination import StandardResultsPagination


class PostCreateAPIView(CreateAPIView):
    serializer_class = PostModelSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class PostListAPIView(ListAPIView):
    serializer_class = PostModelSerializer
    pagination_class = StandardResultsPagination

    def get_queryset(self, *args, **kwargs):
        im_following=self.request.user.profile.get_following()
        qs1 = Post.objects.filter(user__in=im_following)
        qs2 = Post.objects.filter(user=self.request.user)
        qs=(qs1 | qs2).distinct().order_by("-updated_on")
        print(self.request.GET)
        query =self.request.GET.get("q",None)
        if query is not None:
            qs=qs.filter(
                Q(content__icontains=query) |
                Q(user__username__icontains=query)
            )
        return qs