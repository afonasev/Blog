from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView

from . import forms, models


class PostList(ListView):

    template_name = 'posts/post-list.html'
    queryset = models.Post.unhidden().order_by('-created_at')
    paginate_by = 10


class PostDetail(DetailView):

    template_name = 'posts/post-detail.html'

    def get_object(self, queryset=None):
        return get_object_or_404(models.Post, slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'form' not in kwargs:
            context['form'] = forms.CommentForm()
        return context

    # pylint:disable=unused-argument
    def post(self, request, *args, **kwargs):
        # pylint:disable=attribute-defined-outside-init
        self.object = self.get_object()

        form = forms.CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.object
            if request.user.is_authenticated():
                comment.author = request.user
            comment.save()

        return self.render_to_response(self.get_context_data(form=form))


class PostByTagList(PostList):

    def get_queryset(self):
        return super().get_queryset().filter(tags__slug=self.kwargs['slug'])
