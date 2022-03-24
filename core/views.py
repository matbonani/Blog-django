from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy

from .models import Post
from .forms import PostForm


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

