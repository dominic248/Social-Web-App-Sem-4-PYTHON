"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from hashtags.views import HashTagView

from oauth2_provider.views.generic import ProtectedResourceView
from django.http import HttpResponse,JsonResponse
from rest_framework.views import APIView
class ApiEndpoint(APIView):
    def get(self, request, *args, **kwargs):
        print(request.user.username)
        return JsonResponse({'email':request.user.email,'first_name':request.user.get_short_name(),'last_name':request.user.last_name})
        if request.user.is_authenticated: 
            return HttpResponse('Hello there! You are acting on behalf of '+str(request.user))
        else:
            return HttpResponse('Hello! I do not recognize you\n')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('user_registration.urls')),
    path('post/', include('posts.urls', namespace='post')),
    path('tags/<hashtag>/', login_required(HashTagView.as_view()), name='post-hashtags'),
    path('api-auth/', include('rest_framework.urls')),
    path('post/api/', include('posts.api.urls', namespace='post-api')),
    path('profile/api/', include('user_registration.api.urls', namespace='user-api')),
    path('tags/<hashtag>/api/', include('hashtags.api.urls', namespace='hashtag-api')),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('api/hello/', ApiEndpoint.as_view()), 
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
