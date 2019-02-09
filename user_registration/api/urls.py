from django.urls import path,include
from .views import UserPostListAPIView


app_name='user-api'
urlpatterns=[
    # path('', home, name='home'),
    path('', UserPostListAPIView.as_view(), name='user-post-api'),


]