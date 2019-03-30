from rest_framework.generics import ListAPIView
from rest_framework import permissions
from posts.models import Post
from posts.api.serializers import PostModelSerializer
from django.db.models import Q
from rest_framework.views import APIView
from .pagination import StandardResultsPagination
from django.contrib.auth.models import User
from ..models import Profile
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .serializers import UserSerializer

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

class FollowUnfollowAPIView(APIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'username'
    queryset = User.objects.all()
    def get(self,request,slug,format=None):
        message="ERROR"
        toggle_user=get_object_or_404(User,username__iexact=slug)
        if request.user.is_authenticated:
            print("Hey",request.user,toggle_user)
            is_following=Profile.objects.toggle_follow(request.user,toggle_user)
            user_qs=get_object_or_404(User,username=toggle_user)  
            serializer= UserSerializer(user_qs)
            new_serializer_data = dict(serializer.data)
            new_serializer_data.update({'following': is_following})
            new_serializer_data.update({'count':request.user.profile.following.all().count()})
            return Response(new_serializer_data)
        return Response({"message":message},status=400)

class FollowRemoveAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self,request,slug,format=None):
        message="ERROR"
        toggle_user=get_object_or_404(User,username__iexact=slug)
        if request.user.is_authenticated:
            print("Hey",request.user,toggle_user)
            is_following=Profile.objects.toggle_remove_follow(request.user,toggle_user)
            user_qs=get_object_or_404(User,username=toggle_user)  
            serializer= UserSerializer(user_qs)
            new_serializer_data = dict(serializer.data)
            new_serializer_data.update({'following': is_following})
            new_serializer_data.update({'count':request.user.followed_by.all().count()})
            return Response(new_serializer_data)
        return Response({"message":message},status=400)

