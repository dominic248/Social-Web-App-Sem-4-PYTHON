from rest_framework import serializers
from django.utils.timesince import timesince

from posts.models import Post
from user_registration.api.serializers import UserSerializer

class PostModelSerializer(serializers.ModelSerializer):
    user=UserSerializer(read_only=True)
    timesince=serializers.SerializerMethodField()
    likes=serializers.SerializerMethodField()
    did_like=serializers.SerializerMethodField()
    class Meta:
        model=Post
        fields=[
            'id',
            'user',
            'content',
            'image',
            'updated_on',
            'timesince',
            'get_absolute_url',
            'likes',
            'did_like',
        ]

    def get_did_like(self,obj,request=None):
        request=self.context.get("request")
        if request is not None:
            user=request.user
            if user.is_authenticated:
                if user in obj.liked.all():
                    return True
            return False
        return False

    def get_likes(self,obj):
        return obj.liked.all().count()


    def get_timesince(self,obj):
        return timesince(obj.updated_on) + " ago"

