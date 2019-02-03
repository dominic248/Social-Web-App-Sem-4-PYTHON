from django.urls import path,include
from .views import PostListView, PostDetailView, PostCreateView,PostUpdateView,PostDeleteView

app_name='post'
urlpatterns=[
    # path('', home, name='home'),
    path('<int:pk>/', PostDetailView.as_view(), name='detail'),
    path('', PostListView.as_view(), name='list'),
    path('create/', PostCreateView.as_view(), name='create'),
    path('<int:pk>/edit/', PostUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='delete'),
]