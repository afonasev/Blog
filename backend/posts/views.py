from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView

from . import models


class PostList(ListView):

    template_name = 'posts/post-list.html'
    queryset = models.Post.unhidden().order_by('-created_at')
    paginate_by = 10


class PostDetail(DetailView):

    template_name = 'posts/post-detail.html'

    def get_object(self, queryset=None):
        return get_object_or_404(models.Post, slug=self.kwargs['slug'])


class PostByTagList(PostList):

    def get_queryset(self):
        return super().get_queryset().filter(tags__slug=self.kwargs['slug'])
