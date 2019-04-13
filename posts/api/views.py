from rest_framework.generics import ListAPIView,CreateAPIView,DestroyAPIView,UpdateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions,status
from ..models import Post
from .serializers import PostModelSerializer
from django.db.models import Q
from .pagination import StandardResultsPagination
from user_registration.api.serializers import UserSerializer
from django.shortcuts import get_object_or_404
import json
from django.core.exceptions import PermissionDenied

class LikeAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PostModelSerializer
    lookup_field = 'pk'
    def get(self,request,pk,format=None):
        post_qs=Post.objects.filter(pk=pk)
        message="Not allowed"
        if request.user.is_authenticated:
            is_liked=Post.objects.like_toggle(request.user,post_qs.first())
            serializer= PostModelSerializer(post_qs.first())           
            new_serializer_data = dict(serializer.data)
            new_serializer_data.update({'liked':is_liked})
            print(new_serializer_data)
            return Response(new_serializer_data)
        return Response({"message":message},status=400)

class PostDetailAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = StandardResultsPagination
    serializer_class = PostModelSerializer
    lookup_field = 'pk'
    queryset = Post.objects.all()
    def get(self,request,pk):
        post_qs=get_object_or_404(Post,pk=pk)
        serializer= PostModelSerializer(post_qs)
        serialized_data = serializer.data
        serialized_data["user"]["current_user"]=self.request.user.id
        post=Post.objects.all()[0]
        if self.request.user in post.liked.all():
            is_liked=True
        else:
            is_liked=False
        serialized_data["did_like"]=is_liked
        print(serialized_data)
        return Response(serialized_data)
    def delete(self, request,pk):
        print("PK is",pk)
        post_qs=get_object_or_404(Post,pk=pk)
        post_qs.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PostCreateAPIView(CreateAPIView):
    serializer_class = PostModelSerializer
    permission_classes = [permissions.IsAuthenticated]
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class PostListAPIView(ListAPIView):
    serializer_class = PostModelSerializer
    pagination_class = StandardResultsPagination
    def get_serializer_context(self,*args,**kwargs):
        context=super(PostListAPIView,self).get_serializer_context(*args,**kwargs)
        context['request']=self.request
        return context
    def get_queryset(self, *args, **kwargs):
        im_following=self.request.user.profile.get_following()
        qs1 = Post.objects.filter(user__in=im_following)
        qs2 = Post.objects.filter(user=self.request.user)
        qs=(qs1 | qs2).distinct().order_by("-updated_on")
        qsall=Post.objects.all()
        print(self.request.GET)
        query =self.request.GET.get("q",None)
        print("Query is: ",query)
        if query != "":
            qs=qsall.filter(
                Q(content__icontains=query) |
                Q(user__username__icontains=query)
            )
        return qs

class PostDeleteAPIView(DestroyAPIView):
    serializer_class = PostModelSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'pk'
    queryset=Post.objects.all()
    def get_queryset(self,*args,**kwargs):
        data = self.request.is_ajax()
        print(self.request.data)
        pk=json.loads(self.request.data["pk"])
        post=Post.objects.get(pk=pk)
        print(post.user)
        if post.user!=self.request.user:
            raise PermissionDenied
        elif post.user==self.request.user:
            return Post.objects.all()

class PostUpdateAPIView(UpdateAPIView):
    serializer_class = PostModelSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'pk'
    queryset = Post.objects.all()
    def get_queryset(self,*args,**kwargs):
        data = self.request.is_ajax()
        print(self.request.data)
        pk=json.loads(self.request.data["pk"])
        post=Post.objects.get(pk=pk)
        print(post.user,pk)
        if post.user!=self.request.user:
            raise PermissionDenied
        elif post.user==self.request.user:
            return Post.objects.all()

