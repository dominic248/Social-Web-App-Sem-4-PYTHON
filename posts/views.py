from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostModelForm
from django.urls import reverse_lazy
from .mixins import FormUserNeededMixin, UserOwnerMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.db.models import Q

class PostCreateView(FormUserNeededMixin, CreateView):
    template_name = "posts/post_create_view.html"
    form_class = PostModelForm
    # queryset = Post.objects.all()
    # form=PostModelForm
    # fields = ["user","content"]
    # success_url = reverse_lazy("post:list")
    login_url = reverse_lazy("account_login")


class PostUpdateView(LoginRequiredMixin, UserOwnerMixin, UpdateView):
    queryset = Post.objects.all()
    template_name = "posts/post_update_view.html"
    form_class = PostModelForm
    # success_url = reverse_lazy("post:list")


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = "posts/post_delete_view.html"
    success_url = reverse_lazy("post:list")

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.user == self.request.user:
            self.object.delete()
            return HttpResponseRedirect(self.get_success_url())
        else:
            raise PermissionDenied


class PostDetailView(DetailView):
    template_name = 'posts/post_detail_view.html'
    queryset = Post.objects.all()

    def get_object(self):
        print(self.kwargs)
        pk = self.kwargs.get("pk")
        obj = get_object_or_404(Post, id=pk)
        return obj

    def get_context_data(self, *args, **kwargs):
        context = super(PostDetailView, self).get_context_data(*args, **kwargs)
        print(context)
        return context


class PostListView(ListView):
    template_name = 'posts/post_list_view.html'

    def get_queryset(self, *args, **kwargs):
        qs = Post.objects.all()
        print(self.request.GET)
        query =self.request.GET.get("q",None)
        if query is not None:
            qs=qs.filter(
                Q(content__icontains=query) |
                Q(user__username__icontains=query)
            )
        return qs

    def get_context_data(self, *args, **kwargs):
        context = super(PostListView, self).get_context_data(*args, **kwargs)
        context['createForm']=PostModelForm()
        context['create_url']=reverse_lazy("post:create")
        print(context)
        return context
