from django.contrib.auth import get_user_model
from user_registration.models import Profile
from django.urls import reverse_lazy

from rest_framework import serializers

User=get_user_model()

class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = [
            'location',
            'image',
        ]


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    url=serializers.SerializerMethodField()
    class Meta:
        model=User
        fields=[
            'username',
            'first_name',
            'last_name',
            'email',
            'profile',
            'url'
        ]
    def get_url(self,obj):
        return reverse_lazy("user-profile",kwargs={"slug":obj.username})
