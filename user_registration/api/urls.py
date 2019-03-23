from django.urls import path,include
from .views import UserPostListAPIView,FollowUnfollowAPIView,FollowRemoveAPIView


app_name='user-api'
urlpatterns=[
    # path('', home, name='home'),
    path('<slug>/', UserPostListAPIView.as_view(), name='user-post-api'),
    path('<slug>/follow/', FollowUnfollowAPIView.as_view(), name='user-follow-toggle'),
    path('<slug>/followremove/', FollowRemoveAPIView.as_view(), name='user-follow-remove'),

]