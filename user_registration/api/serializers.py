from django.contrib.auth import get_user_model
from user_registration.models import Profile
from django.urls import reverse_lazy
from allauth.socialaccount.models import SocialAccount
from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault

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
    # current_user =  serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault(),context={'request': request})
    current_user = serializers.SerializerMethodField('curruser')

    class Meta:
        model=User
        fields=[
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'profile',
            'url',
            'current_user',
        ]

    # Use this method for the custom field
    def curruser(self, obj):
        try:
            return self.context['request'].user.id
        except:
            pass


    def get_url(self,obj):
        return reverse_lazy("user-profile",kwargs={"slug":obj.username})



