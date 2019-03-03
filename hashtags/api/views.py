from rest_framework.generics import ListAPIView
from rest_framework import permissions
from posts.models import Post
from posts.api.serializers import PostModelSerializer
from django.db.models import Q
from .pagination import StandardResultsPagination
from ..models import HashTag

class TagListAPIView(ListAPIView):
    queryset = Post.objects.all().order_by("-updated_on")
    serializer_class = PostModelSerializer
    pagination_class = StandardResultsPagination

    def get_serializer_context(self,*args,**kwargs):
        context=super(TagListAPIView,self).get_serializer_context(*args,**kwargs)
        context['request']=self.request
        return context

    def get_queryset(self, *args, **kwargs):
        hashtag=self.kwargs.get("hashtag")
        hashtag_obj=None
        try:
            hashtag_obj=HashTag.objects.get_or_create(tag=hashtag)[0]
        except:
            pass
        if hashtag_obj:
            qs=hashtag_obj.get_posts()
            query = self.request.GET.get("q",None)
            if query is not None:
                qs=qs.filter(
                    Q(content__icontains=query) |
                    Q(user__username__icontains=query)
                )
            return qs
        return None