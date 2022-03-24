from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy

from .models import Post


class IndexView(ListView):
    model = Post
    template_name = 'index.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'artigo_detail.html'


class AddPostView(CreateView):
    model = Post
    template_name = 'add_post.html'
    fields = ['autor', 'titulo', 'body']
    success_url = reverse_lazy('index')