from django.urls import path,include
from .views import PostListAPIView,PostCreateAPIView,\
    LikeAPIView,PostDetailAPIView,PostDeleteAPIView,PostUpdateAPIView

app_name='posts-api'
urlpatterns=[
    path('', PostListAPIView.as_view(), name='list'),
    path('<int:pk>/', PostDetailAPIView.as_view(), name='detail'),
    path('<int:pk>/delete/', PostDeleteAPIView.as_view(), name='delete'),
    path('<int:pk>/update/', PostUpdateAPIView.as_view(), name='update'),
    path('<int:pk>/like/', LikeAPIView.as_view(), name='like'),
    path('create/', PostCreateAPIView.as_view(), name='create'),

    # path('<int:pk>/edit/', PostUpdateView.as_view(), name='update'),
    # path('<int:pk>/delete/', PostDeleteView.as_view(), name='delete'),

]