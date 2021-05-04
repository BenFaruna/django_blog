from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView

from .models import BlogPost, Comment


class BlogListView(ListView):
    model = BlogPost
    template_name = 'home.html'


class BlogDetailView(DetailView):
    model = BlogPost
    template_name = 'blog_detail.html'


class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = BlogPost
    fields = ('title', 'body',)
    template_name = 'blog_edit.html'
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class BlogCommentView(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = 'blog_comment.html'
    fields = ('comment',)
    login_url = 'login'
    success_url = reverse_lazy('blog_detail')


class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = BlogPost
    template_name = 'blog_delete.html'
    success_url = reverse_lazy('home')
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = BlogPost
    template_name = 'blog_new.html'
    fields = ('title', 'body')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
