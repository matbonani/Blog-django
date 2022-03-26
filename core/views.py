from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy, reverse

from .models import Post
from .forms import PostForm, EditForm


class IndexView(ListView):
    model = Post
    template_name = 'index.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'artigo_detail.html'


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    # fields = ['autor', 'titulo', 'body']
    success_url = reverse_lazy('index')


class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'atualizando.html'
    # fields = ['titulo', 'body']
    success_url = reverse_lazy('index')



