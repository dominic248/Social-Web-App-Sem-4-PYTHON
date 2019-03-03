from django.shortcuts import render,redirect,HttpResponseRedirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import DetailView
from django.contrib.auth import get_user_model
from django.views import View
from .models import Profile
User=get_user_model()

class UserDetailView(DetailView):
    queryset = User.objects.all()
    template_name ="user/user_profile.html"
    slug_field='username'

    def get_context_data(self, *args, **kwargs):
        context = super(UserDetailView, self).get_context_data(*args, **kwargs)
        context['following']=Profile.objects.is_following(self.request.user,self.kwargs['slug'])
        print(self.args, self.kwargs,self.request.user,self.kwargs['slug'])
        print(context)
        return context

class UserFollowView(View):
    def get(self,request,slug,*args,**kwargs):
        print(*args,**kwargs)
        toggle_user=get_object_or_404(User,username__iexact=slug)
        if request.user.is_authenticated:
            is_following=Profile.objects.toggle_follow(request.user,toggle_user)
        return redirect("user-profile",slug=self.request.user.username)

# Create your views here.

def home(request):
    count=User.objects.count()
    return render(request,'home.html',{
        'user_count':count
    })



@login_required(login_url='account_login')
def secret_page(request):
    return render(request,'secret_page.html')

@login_required(login_url='account_login')
def settings(request):
    return HttpResponseRedirect(reverse("account_email"))




