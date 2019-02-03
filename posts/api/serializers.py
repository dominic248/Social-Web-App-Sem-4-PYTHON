from rest_framework import serializers
from django.utils.timesince import timesince

from posts.models import Post
from user_registration.api.serializers import UserSerializer

class PostModelSerializer(serializers.ModelSerializer):
    user=UserSerializer(read_only=True)
    timesince=serializers.SerializerMethodField()
    class Meta:
        model=Post
        fields=[
            'user',
            'content',
            'created_on',
            'timesince',
            'get_absolute_url'
        ]

    def get_timesince(self,obj):
        return timesince(obj.created_on) + " ago"