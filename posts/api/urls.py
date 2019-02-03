from django.urls import path,include
from .views import PostListAPIView,PostCreateAPIView

app_name='posts-api'
urlpatterns=[
    # path('', home, name='home'),
    # path('<int:pk>/', PostDetailView.as_view(), name='detail'),
    path('', PostListAPIView.as_view(), name='list'),
    path('create/', PostCreateAPIView.as_view(), name='create'),
    # path('<int:pk>/edit/', PostUpdateView.as_view(), name='update'),
    # path('<int:pk>/delete/', PostDeleteView.as_view(), name='delete'),

]