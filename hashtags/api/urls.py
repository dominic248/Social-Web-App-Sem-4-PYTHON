from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import TagListAPIView

app_name = 'hashtag-api'
urlpatterns = [
    path('', login_required(TagListAPIView.as_view()), name='tag-api'),
]
