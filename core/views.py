from django.urls import reverse_lazy, reverse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect

from .models import Post
from .forms import PostForm, UpdateForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class IndexView(ListView):
    model = Post
    template_name = 'index.html'
    ordering = ['-id']
    # ordering = ['hora']


class DetailPostView(DetailView):
    model = Post
    template_name = 'artigo_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(DetailPostView, self).get_context_data(**kwargs)

        stuf = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuf.total_likes()

        liked = False
        if stuf.likes.filter(id=self.request.user.id).exists():
            liked = True

        context['total_likes'] = total_likes
        context['liked'] = liked
        return context


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    # fields = ['autor', 'titulo', 'body']
    success_url = reverse_lazy('index')


class UpdatePostView(UpdateView):
    model = Post
    form_class = UpdateForm
    template_name = 'update_post.html'
    # fields = ['titulo', 'body']
    success_url = reverse_lazy('index')


class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('index')


def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('post_detail', args=[str(pk)]))
