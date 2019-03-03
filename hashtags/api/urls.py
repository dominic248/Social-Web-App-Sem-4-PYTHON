from django.urls import path,include
from .views import TagListAPIView

app_name='hashtag-api'
urlpatterns=[
    path('', TagListAPIView.as_view(), name='tag-api'),

]